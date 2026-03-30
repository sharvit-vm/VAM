# state -> uses typeddict and acts as shared memory in the workflows 
from typing import TypedDict

class MyState(TypedDict):
    question: str
    answer: str 


def generateAnswer(state: MyState):
    question = state["question"]
    answer = f"Answer: {question}"
    return {"answer": answer}