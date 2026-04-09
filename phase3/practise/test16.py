from andromeda.utils import get_chat_model
from andromeda.config import ModelConfig
from andromeda import HumanMessage

chat_model = get_chat_model(
    ModelConfig(name="qwen2.5",provider="ollama",other_args={"base_url": "http://localhost:11434", "temperature": 0.2},))
response = chat_model.invoke([HumanMessage(content="One-sentence summary of Andromeda.")])
print(response.content)