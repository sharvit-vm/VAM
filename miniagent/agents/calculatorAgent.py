from .baseAgent import Agent
import re
class CalculatorAgent(Agent):

    def extract_expression(self, query: str):
        match = re.search(r"\d+(\s*[\+\-\*/]\s*\d+)+", query)
        return match.group() if match else None
    
    def canHandle(self, query: str) -> bool:
        return self.extract_expression(query) is not None

    def run(self, query: str) -> str:
        expression = self.extract_expression(query)
        if not expression:
            return "Invalid math expression"
        try:
            result = eval(expression)
            return f"[CalculatorAgent] Result: {result}"
        except Exception:
            return "Invalid math expression"