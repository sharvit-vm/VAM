import asyncio
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    text: str

def step1(state: State):
    return {"text": "Hello"}

def step2(state: State):
    return {"text": state["text"] + " World"}

builder = StateGraph(State)

builder.add_node("step1", step1)
builder.add_node("step2", step2)

builder.add_edge(START, "step1")
builder.add_edge("step1", "step2")
builder.add_edge("step2", END)

graph = builder.compile()

async def run():
    async for event in graph.astream_events({"text": ""}):
        print(event)

asyncio.run(run())