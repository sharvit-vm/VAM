from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command

class State(TypedDict):
    topic: str
    draft: str
    final: str

def writer(state: State):
    return Command(goto="editor", update={"draft": f"Draft content on {state['topic']}"})

def editor(state: State):
    return {"final": state["draft"]+"(edited)"}

graph = StateGraph(State)
graph.add_node("writer", writer)
graph.add_node("editor", editor)
graph.add_edge(START, "writer")
graph.add_edge("editor", END)
graphapp = graph.compile()
result = graphapp.invoke({"topic": "AI"})
print(result)
