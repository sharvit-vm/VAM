from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class MyState(TypedDict):
    question: str
    category: str
    answer: str

def classify(state: MyState):
    question = state["question"]
    if "calculate" in question.lower():
        category = "math"
    else:
        category = "general"
    return {"category": category}
def math_node(state: MyState):
    return {"answer": "This is a math answer (fake logic)"}
def general_node(state: MyState):
    return {"answer": f"General answer for: {state['question']}"}

def router(state: MyState):
    if state["category"] == "math":
        return "math_node"
    return "general_node"
graph = StateGraph(MyState)
graph.add_node("classifier", classify)
graph.add_node("math_node", math_node)
graph.add_node("general_node", general_node)

graph.add_edge(START, "classifier")
graph.add_conditional_edges("classifier", router)
graph.add_edge("math_node", END)
graph.add_edge("general_node", END)
app = graph.compile()
result = app.invoke({"question": "Calculate 5 + 5"})
print(result)