from abc import ABC, abstractmethod
class Agent(ABC):
    def __init__(self, name: str):
        self.name = name
        self._calls = 0
    @abstractmethod
    def canHandle(self, query: str) -> bool:
        #Return True if this agent can handle the query.
        pass
    @abstractmethod
    def run(self, query: str) -> str:
        #Process the query and return response.
        pass
    def __call__(self, query: str) -> str:
        #Allows agent to be called like a function
        self._calls += 1
        return self.run(query)
    def __len__(self):
        #Returns how many times agent was called.
        return self._calls
    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"