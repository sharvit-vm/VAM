import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "rag-project"
def get_llm():
    return ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini"
    )