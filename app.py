import os
import sys
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the refactored news summarization function
try:
    from newssummarizer import summarize_news_by_topic
except ImportError as e:
    print(f"Error importing summarize_news_by_topic: {e}")
    sys.exit(1)

app = FastAPI(title="AI News Summarizer API")

# Mount the static directory to serve CSS, JS, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Request schema
class SummarizeRequest(BaseModel):
    topic: str

# Serve the frontend index.html
@app.get("/")
def read_root():
    # Return index.html from static folder
    index_path = os.path.join("static", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    raise HTTPException(status_code=404, detail="Frontend index.html not found.")

# Summarize API endpoint
@app.post("/api/summarize")
def summarize(req: SummarizeRequest):
    topic = req.topic.strip()
    if not topic:
        raise HTTPException(status_code=400, detail="Topic cannot be empty.")
    
    try:
        # Call the summarizer function
        summary = summarize_news_by_topic(topic)
        return {"summary": summary}
    except Exception as e:
        print(f"Error during summarization for '{topic}': {e}")
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred while summarizing: {str(e)}"
        )

if __name__ == "__main__":
    # Start uvicorn server on localhost:8000
    print("Starting AI News Summarizer Server at http://localhost:8000")
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
