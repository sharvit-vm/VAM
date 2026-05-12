from andromeda.core.agent import Agent
from andromeda.config import AgentConfig, ModelConfig

agent = Agent(
    AgentConfig(name="chat_agent", model=ModelConfig(name="qwen3:8b", provider="ollama"))
)

agent.chat("My name is Omar.")
second = agent.chat("What is my name?")

print("Assistant answer:", second[-1].content)  # use -1, not -2
print("Stored messages:", len(agent.memory))
print("Memory snapshot:", [getattr(m, "content", str(m)) for m in agent.memory])