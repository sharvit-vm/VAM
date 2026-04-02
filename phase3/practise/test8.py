from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class genState(TypedDict):
    text: str

def generate(state: genState):
    return {"text": "This is AI generated content"}

genbuilder = StateGraph(genState)
genbuilder.add_node("generate", generate)
genbuilder.add_edge(START, "generate")
genbuilder.add_edge("generate", END)
genapp = genbuilder.compile()

class reviewState(TypedDict):
    text: str
    approved: bool

def review(state: reviewState):
    return {"approved": True}

reviewbuilder = StateGraph(reviewState)
reviewbuilder.add_node("review", review)
reviewbuilder.add_edge(START, "review")
reviewbuilder.add_edge("review", END)
reviewapp = reviewbuilder.compile()

class MainState(TypedDict):
    text: str
    approved: bool
builder = StateGraph(MainState)
builder.add_node("generate", genapp)      
builder.add_node("review", reviewapp)
builder.add_edge(START, "generate")
builder.add_edge("generate", "review")
builder.add_edge("review", END) 
app = builder.compile()
print(app.invoke({}))