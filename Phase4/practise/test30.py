from andromeda.utils import get_chat_model, get_embedding_model
from andromeda.config import ModelConfig 
from andromeda import HumanMessage
from dotenv import load_dotenv
load_dotenv()

chat_model = get_chat_model(
    ModelConfig(
        name = "gpt-4o-mini",
        provider = "openai"
    )
)

messages = [HumanMessage(content = "Explain AI agents in 20 words")]

chat_response = chat_model.invoke(messages)
print(chat_response.content)
