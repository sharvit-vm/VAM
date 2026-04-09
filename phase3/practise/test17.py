from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

class State(TypedDict):
    messages: list

def chatbot(state: State):
    return {"messages": state["messages"] + [{"role": "assistant", "content": "Hello!"}]}
builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)
memory = MemorySaver()
graph = builder.compile(checkpointer=memory)
config = {"configurable": {"thread_id": "user1"}}
print(graph.invoke({"messages": [{"role": "user", "content": "Hi"}]}, config))
print(graph.invoke({"messages": []}, config))