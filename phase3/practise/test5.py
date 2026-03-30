from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class SupportState(TypedDict):
    query: str
    intent: str
    response: str

def classify_intent(state: SupportState):
    query = state["query"].lower()
    if "price" in query or "cost" in query:
        intent = "billing"
    elif "how" in query or "what" in query:
        intent = "faq"
    else:
        intent = "human"
    return {"intent": intent}

def faq_node(state: SupportState):
    return {"response": "This is an FAQ answer."}

def billing_node(state: SupportState):
    return {"response": "Redirecting to billing support."}

def human_node(state: SupportState):
    return {"response": "Connecting you to a human agent..."}

def router(state: SupportState):
    if state["intent"] == "faq":
        return "faq_node"
    elif state["intent"] == "billing":
        return "billing_node"
    else:
        return "human_node"

graph = StateGraph(SupportState)
graph.add_node("classifier", classify_intent)
graph.add_node("faq_node", faq_node)
graph.add_node("billing_node", billing_node)
graph.add_node("human_node", human_node)
graph.add_edge(START, "classifier")
graph.add_conditional_edges("classifier", router)
graph.add_edge("faq_node", END)
graph.add_edge("billing_node", END)
graph.add_edge("human_node", END)
app = graph.compile()

result = app.invoke({"query": "I want to know about my subscription?"})
print(result)