
from .baseAgent import Agent


class SearchAgent(Agent):
    def can_handle(self, query: str) -> bool:
    
        return not any(op in query for op in "+-*/")

    def run(self, query: str) -> str:
        return f"[SearchAgent] Searching for: {query}"