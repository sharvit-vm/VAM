from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import InMemorySaver
from typing_extensions import TypedDict

class State(TypedDict):
    text: str
    approved: bool


def generate(state: State):
    return {"text": "This is AI generated content"}

def review(state: State):
    decision = interrupt(f"Review this text:\n{state['text']}\nApprove? (yes/no)")
    return {"approved": decision.lower() == "yes"}

def final(state: State):
    if state["approved"]:
        print("Content Approved")
    else:
        print("Content Rejected")
    return {}
    
def decide_next(state: State):
    if state["approved"]:
        return "final"
    else:
        return "generate"
builder = StateGraph(State)
builder.add_node("generate", generate)
builder.add_node("review", review)
builder.add_node("final", final)
builder.add_edge(START, "generate")
builder.add_edge("generate", "review")
builder.add_conditional_edges("review",decide_next)
builder.add_edge("final", END)
memory = InMemorySaver()
graph = builder.compile(checkpointer=memory)
config = {"configurable": {"thread_id": "1"}}
result = graph.invoke({}, config=config)
while "__interrupt__" in result:
    print(result["__interrupt__"][0].value)
    user_input = input("Enter your decision: ")
    result = graph.invoke(Command(resume=user_input),config=config)