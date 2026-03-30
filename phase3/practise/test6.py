from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import InMemorySaver

class State(TypedDict):
    content: str
    approved: bool

def to_bool(value: str) -> bool:
    value = value.strip().lower()
    if value in ["yes", "y", "true", "1"]:
        return True
    elif value in ["no", "n", "false", "0"]:
        return False
    else:
        raise ValueError("Invalid input. Please enter yes/no.")

def generate(state: State):
    return {"content": "AI Generated Content"}

def approval(state: State):
    decision = interrupt(f"Approve this: {state['content']} (yes/no)")
    approved = to_bool(decision)
    return {"approved": approved}

def publish(state: State):
    return {"content": "Published"}

def reject(state: State):
    return {"content": "Rejected"}

def router(state: State):
    if state["approved"]:
        return "publish"
    return "reject"

graph = StateGraph(State)
graph.add_node("generate", generate)
graph.add_node("approval", approval)
graph.add_node("publish", publish)
graph.add_node("reject", reject)
graph.add_edge(START, "generate")
graph.add_edge("generate", "approval")
graph.add_conditional_edges("approval", router)
graph.add_edge("publish", END)
graph.add_edge("reject", END)
checkpointer = InMemorySaver()

app = graph.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "1"}}
print("Graph Starting point.\n")
result = app.invoke({"content": "", "approved": False},config=config)
print("Graph paused. Waiting for approval...\n")
while True:
    user_input = input("Enter approval (yes/no): ")
    try:
        to_bool(user_input) 
        break
    except ValueError:
        print("Invalid input. Please type yes or no.")
result = app.invoke(Command(resume=user_input),config=config)
print("\nFinal Result:")
print(result)