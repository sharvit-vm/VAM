from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1. State
class State(TypedDict):
    content: str
    approved: bool

# 2. Generate initial content
def generate(state: State):
    return {"content": "Draft content"}

# 3. Review node
def review(state: State):
    print("Reviewing:", state["content"])
    decision = input("Approve? (yes/no): ")
    
    approved = decision.strip().lower() == "yes"
    
    return {"approved": approved}

# 4. Fix node
def fix(state: State):
    return {"content": state["content"] + " (improved)"}

# 5. Publish node
def publish(state: State):
    return {"content": "Final Published Content"}

# 6. Router
def router(state: State):
    if state["approved"]:
        return "publish"
    return "fix"

# 7. Build graph
graph = StateGraph(State)

graph.add_node("generate", generate)
graph.add_node("review", review)
graph.add_node("fix", fix)
graph.add_node("publish", publish)

# Flow
graph.add_edge(START, "generate")
graph.add_edge("generate", "review")

# Conditional branching
graph.add_conditional_edges("review", router)

# 🔁 Loop back if not approved
graph.add_edge("fix", "review")

# End
graph.add_edge("publish", END)

# Compile
app = graph.compile()

# Run
result = app.invoke({
    "content": "",
    "approved": False
})

print("\nFinal Result:")
print(result)