from typing import Dict, Any 
from andromeda.tools import tool
from andromeda.core.agent import Agent
from andromeda.config import AgentConfig, ModelConfig
from andromeda import HumanMessage
from dotenv import load_dotenv
load_dotenv()

@tool 
def echo_tool(text: str)->Dict[str, Any]:
    """echo text back;"""
    return {"echo": text}

cfg = AgentConfig(
    name = "echo_agent",
    model = ModelConfig(
        name = "gpt-4o-mini",
        provider = "openai"
    ),
    tools = [echo_tool],
    prompt = "Use tools when neeeded"
)

agent = Agent(cfg)
messages = [HumanMessage(content = "Use the echo tool to repeat 'Andromeda'.")]
result = agent.invoke(messages)
print(result[-1].content)
