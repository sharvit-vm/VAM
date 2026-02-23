from typing import List
from agents.baseAgent import Agent
class Router:
    def __init__(self, agents: List[Agent]):
        self.agents = agents
    def route(self, query: str) -> str:
        for agent in self.agents:
            if agent.can_handle(query):
                return agent(query) 
        return "No suitable agent found."