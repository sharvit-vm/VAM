from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    api_url: str = os.getenv("API_URL", "")
    api_key: str = os.getenv("API_KEY", "")

settings = Settings()