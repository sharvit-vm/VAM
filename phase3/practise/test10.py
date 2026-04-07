from typing import TypedDict 
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command

class State(TypedDict):
    query : str
    answer : str

def superviser(state: State):
    if "code" in state["query"].lower():
        return Command(goto="coder")
    else: 
        return Command(goto="general")

def coder(state: State):
    return {"answer": "This is a code related answer"}

def general(state: State):
    return {"answer": "This is a general question answer"}

graph = StateGraph(State)
graph.add_node("superviser", superviser)
graph.add_node("coder", coder)
graph.add_node("general", general)
graph.add_edge(START, "superviser") 
graph.add_edge("coder", END)
graph.add_edge("general", END)
graphapp = graph.compile()
result = graphapp.invoke({"query": "What is code?"})
print(result)