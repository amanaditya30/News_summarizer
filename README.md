# AI News Summarizer Dashboard 📰✨

A premium web-based application designed to search the web for the latest updates on any given topic and synthesize them into clean, actionable bullet-point summaries in real-time.

Built with a high-performance **FastAPI** backend and an elegant, responsive **glassmorphic dark-mode** frontend.

---

## 🚀 Features

- **Real-Time Web Search**: Integrates Tavily AI Search to fetch the most recent news on the internet.
- **Instant AI Summarization**: Uses LangChain and Groq's super-fast `Llama-3.1-8b-instant` model to summarize search results into structured bullet points.
- **Premium Glassmorphic UI**: Beautiful custom CSS theme featuring floating gradient glowing orbs, responsive layouts, checkmark lists, and clean typography (`Outfit` & `Inter`).
- **Interactive Quick Tags**: One-click quick suggestions for trending topics (e.g. AI, Space Exploration, Robotics).
- **Clipboard Integration**: Easily copy the generated summaries with one click.

---

## 🛠️ Tech Stack

- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Backend**: FastAPI (Python 3.10+)
- **AI/LLM Stack**: LangChain, LangChain Community (Tavily Search), LangChain Groq (Llama 3.1)
- **Environment**: Python Dotenv

---

## 📦 Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd Runnable
```

### 2. Set Up a Virtual Environment
```bash
python -m venv .venv
# Activate on Windows (Cmd/PowerShell)
.venv\Scripts\activate
# Activate on macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your API credentials:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 5. Run the Application
Start the FastAPI server using Uvicorn:
```bash
python app.py
```

Open your browser and navigate to:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## 📂 Project Structure

```
├── static/
│   ├── index.html   # Main dashboard layout
│   ├── style.css    # Premium glassmorphic styling
│   └── app.js       # API calls and rendering logic
├── app.py           # FastAPI Web Server
├── newssummarizer.py # Core LangChain search & summary logic
├── requirements.txt # Project dependencies
├── .gitignore       # Git exclusion rules
└── README.md        # Project documentation
```
