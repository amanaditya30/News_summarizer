import os
import sys
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key or api_key == "your_groq_api_key_here":
    print("Error: GROQ_API_KEY is not set or is still the placeholder. Please add your Groq API key to the .env file.", file=sys.stderr)
    sys.exit(1)

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

promt = ChatPromptTemplate.from_template(
    "Explain {topic} in a few words"
)

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

chain = promt | model | parser

result = chain.invoke("Machine Learning")

print(result)
