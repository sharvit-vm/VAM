from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    streaming=True
)

async def generate_ai_response():

    async for chunk in llm.astream("Explain AI agents"):

        yield chunk.content

@app.get("/chat")
async def chat():

    return StreamingResponse(
        generate_ai_response(),
        media_type="text/event-stream"
    )