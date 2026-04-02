from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class approvalState(TypedDict):
    approved: bool

def approve(state: approvalState):
    return {"approved": True}

approvalBuilder = StateGraph(approvalState)
approvalBuilder.add_node("approve", approve)        
approvalBuilder.add_edge(START, "approve")
approvalBuilder.add_edge("approve", END)
approvalApp = approvalBuilder.compile()

class mainState(TypedDict):
    approved: bool
builder = StateGraph(mainState)
builder.add_node("approve1",approvalApp)  
builder.add_node("approve2",approvalApp)  
builder.add_edge(START, "approve1")
builder.add_edge("approve1", "approve2")
builder.add_edge("approve2", END)
app = builder.compile()
print(app.invoke({}))