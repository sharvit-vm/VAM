from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph, START, END

def merge_dict(old, new):
    return {**old, **new}

class MyState(TypedDict):
    messages: Annotated[list, add] #old+new appended in list
    score: Annotated[int, add] # old+new addition
    data: Annotated[dict, merge_dict]
    answer: str # answer will be overwritten

def node1(state: MyState):
    return {"messages": ["Hello"],"score": 1,"data": {"a": 1},"answer": "First answer"}

def node2(state: MyState):
    return {"messages": ["World"],"score": 2,"data": {"b": 2},"answer": "Final answer"}
graph = StateGraph(MyState)
graph.add_node("n1", node1)
graph.add_node("n2", node2)
graph.add_edge(START, "n1")
graph.add_edge("n1", "n2")
graph.add_edge("n2", END)
app = graph.compile()
result = app.invoke({
    "messages": [],
    "score": 0,
    "data": {},
    "answer": ""
})
print(result)