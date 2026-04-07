from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command

class State(TypedDict):
    attempts: int
    success: bool

def agent(state: State):
    if state["attempts"] < 3:
        return Command(
            goto="agent",
            update={"attempts": state["attempts"] + 1})
    else:
        return {"success": True}
builder = StateGraph(State)
builder.add_node("agent", agent)
builder.add_edge(START, "agent")
builder.add_edge("agent", END)
graph = builder.compile()
print(graph.invoke({"attempts": 0, "success": False}))