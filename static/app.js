document.addEventListener('DOMContentLoaded', () => {
    const summarizeForm = document.getElementById('summarize-form');
    const newsTopicInput = document.getElementById('news-topic-input');
    const submitBtn = document.getElementById('submit-btn');
    
    const loadingState = document.getElementById('loading-state');
    const errorCard = document.getElementById('error-card');
    const errorMessage = document.getElementById('error-message');
    const resultsCard = document.getElementById('results-card');
    
    const resultTopicName = document.getElementById('result-topic-name');
    const summaryList = document.getElementById('summary-list');
    const copyBtn = document.getElementById('copy-btn');
    const tagButtons = document.querySelectorAll('.tag-btn');

    // Handle suggestion tags
    tagButtons.forEach(button => {
        button.addEventListener('click', () => {
            const topic = button.getAttribute('data-topic');
            newsTopicInput.value = topic;
            triggerSummarization(topic);
        });
    });

    // Form submission
    summarizeForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const topic = newsTopicInput.value.trim();
        if (topic) {
            triggerSummarization(topic);
        }
    });

    // Main fetch & UI transition function
    async function triggerSummarization(topic) {
        // Reset states
        hideElement(resultsCard);
        hideElement(errorCard);
        showElement(loadingState);
        
        // Disable inputs
        newsTopicInput.disabled = true;
        submitBtn.disabled = true;
        
        try {
            const response = await fetch('/api/summarize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ topic: topic })
            });
            
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.detail || 'Failed to fetch summary');
            }
            
            // Render Results
            renderSummary(topic, data.summary);
            
        } catch (error) {
            console.error('Error fetching summary:', error);
            errorMessage.textContent = error.message;
            showElement(errorCard);
        } finally {
            // Re-enable inputs
            hideElement(loadingState);
            newsTopicInput.disabled = false;
            submitBtn.disabled = false;
        }
    }

    // Parse backend response and render bullet points
    function renderSummary(topic, summaryText) {
        resultTopicName.textContent = `Summary: ${topic}`;
        summaryList.innerHTML = '';
        
        // Clean markdown bullets and split by lines
        const lines = summaryText.split('\n');
        let index = 0;
        
        lines.forEach(line => {
            let cleanLine = line.trim();
            
            // Remove markdown list tokens at the start (e.g. *, -, •, or digits like 1.)
            cleanLine = cleanLine.replace(/^([*\-•\s]|\d+\.)\s*/, '').trim();
            
            // Ignore empty lines or headers
            if (cleanLine.length > 3 && !cleanLine.startsWith('#')) {
                const li = document.createElement('li');
                li.textContent = cleanLine;
                // Add staggered animation delay
                li.style.animationDelay = `${index * 0.1}s`;
                summaryList.appendChild(li);
                index++;
            }
        });
        
        if (summaryList.children.length === 0) {
            // Fallback if cleaning removed all lines or returned plain paragraph
            const li = document.createElement('li');
            li.textContent = summaryText;
            summaryList.appendChild(li);
        }
        
        showElement(resultsCard);
    }

    // Copy to clipboard functionality
    copyBtn.addEventListener('click', () => {
        const listItems = Array.from(summaryList.querySelectorAll('li'));
        const textToCopy = listItems.map(li => `• ${li.textContent}`).join('\n');
        
        navigator.clipboard.writeText(textToCopy)
            .then(() => {
                const originalHtml = copyBtn.innerHTML;
                copyBtn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
                copyBtn.classList.add('copied');
                
                setTimeout(() => {
                    copyBtn.innerHTML = originalHtml;
                    copyBtn.classList.remove('copied');
                }, 2000);
            })
            .catch(err => {
                console.error('Could not copy text: ', err);
            });
    });

    // Helper functions for visibility
    function showElement(el) {
        el.classList.remove('hidden');
    }
    
    function hideElement(el) {
        el.classList.add('hidden');
    }
});
