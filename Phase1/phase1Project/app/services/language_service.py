import os
import httpx
from dotenv import load_dotenv

load_dotenv()
class LanguageService:
    def __init__(self):
        self.url = os.getenv("API_URL")
        self.api_key = os.getenv("API_KEY")
        if not self.url or not self.api_key:
            raise ValueError("Missing LANGUAGE_API configuration")

    async def detect_language(self, text: str) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.url, headers={"X-Api-Key": self.api_key},params={"text": text[:500]},timeout=10.0)
            response.raise_for_status()
            data = response.json()
            return data.get("language", "unknown")