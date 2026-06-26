import os
import sys
from dotenv import load_dotenv
load_dotenv()

# Verify api keys are set
groq_key = os.getenv("GROQ_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")
if not groq_key or groq_key == "your_groq_api_key_here":
    print("Error: GROQ_API_KEY is not set or is still the placeholder. Please configure it in .env file.", file=sys.stderr)
    sys.exit(1)
if not tavily_key:
    print("Error: TAVILY_API_KEY is not set. Please configure it in .env file.", file=sys.stderr)
    sys.exit(1)

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

search_tool = TavilySearchResults(max_result=5)
llm = ChatGroq(model="llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_template(
    """You are a helpful assistant.
    Summarize the latest news about the topic from these search results. Provide the response as clear, bulleted points.
    
    Search results:
    {news}
    """
)

chain = prompt | llm | StrOutputParser()

def summarize_news_by_topic(topic: str) -> str:
    """
    Searches for the latest news on a topic using Tavily, and returns a bullet point summary.
    """
    # Search for latest news on the given topic
    search_query = f"Latest news about {topic}"
    news_result = search_tool.run(search_query)
    
    # Run the summary chain
    result = chain.invoke({"news": news_result})
    return result

if __name__ == "__main__":
    test_topic = "Artificial Intelligence"
    print(f"Summarizing latest news for topic: '{test_topic}'...")
    print(summarize_news_by_topic(test_topic))
