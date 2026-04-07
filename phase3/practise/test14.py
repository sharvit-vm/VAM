from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    status: str

def step1(state: State):
    print("Running Step 1")
    return {"status": "Step 1 done"}

def step2(state: State):
    print("Running Step 2")
    return {"status": "Step 2 done"}

builder = StateGraph(State)

builder.add_node("step1", step1)
builder.add_node("step2", step2)

builder.add_edge(START, "step1")
builder.add_edge("step1", "step2")
builder.add_edge("step2", END)

graph = builder.compile()

for event in graph.stream({"status": ""}):
    print("Progress:", event)