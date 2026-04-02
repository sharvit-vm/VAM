from typing import TypedDict
from langgraph.graph import StateGraph, START, END

#state 
class MyState(TypedDict):
    question: str
    answer: str
    
def generate_answer(state: MyState):
    question = state["question"]
    answer = f"Generated answer for: {question}"
    return {"answer": answer}
    
graph = StateGraph(MyState)
graph.add_node("generator", generate_answer)
graph.add_edge(START, "generator")
graph.add_edge("generator", END)
app = graph.compile()
result = app.ainvoke({"question": 12})
print(result)