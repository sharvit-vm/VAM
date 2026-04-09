from typing import TypedDict 
from langgraph.graph import StateGraph,START,END 
from langgraph.checkpoint.sqlite import SqliteSaver 

class State(TypedDict):
    messages: list 

def chatbot(state:State):
    return {
        "messages":state["messages"]+[
            {"role":"assistant","content":"stored reply"}
        ]
    }

builder = StateGraph(State)
builder.add_node("chatbot",chatbot)
builder.add_edge(START,"chatbot")
builder.add_edge("chatbot",END)

with SqliteSaver.from_conn_string("memory.db") as memory:
    graph = builder.compile(checkpointer = memory)
    config = {"configurable": {"thread_id": "user1"}}
    result = graph.invoke({"messages":[{"role":"user","content":"hello"}]},config )
    print(result)