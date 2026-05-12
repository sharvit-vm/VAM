from andromeda.utils import get_embedding_model 
from andromeda.config import ModelConfig
from dotenv import load_dotenv
load_dotenv()
embedding_model = get_embedding_model(
    ModelConfig(
        name="text-embedding-3-small",
        provider = "openai",
        
    )
)

vector = embedding_model.embed_query("who is sharvit kashikar")
print(len(vector),"dimensions")