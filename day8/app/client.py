import httpx
from typing import Dict
from .config import Settings
from .model import LLMRequest, LLMResponse
from .exceptions import (
    AuthenticationError,
    RateLimitError,
    APIResponseError,
)
from .retry import async_retry
class AsyncLLMClient:
    def __init__(self):
        self.settings = Settings.load() # to load api key and other settings!
        self.headers = {
            "Authorization": f"Bearer {self.settings.api_key}",
            "Content-Type": "application/json", #because we need json in response. 
        }
    @async_retry(max_retries=3)
    async def make_request(self, payload: Dict) -> Dict:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(self.settings.base_url,headers=self.headers, json=payload)
        if response.status_code == 401:
            raise AuthenticationError("Invalid API key")
        if response.status_code == 429:
            raise RateLimitError("Rate limit exceeded")
        if response.status_code >= 500:
            raise APIResponseError("Server error")
        if response.status_code != 200:
            raise APIResponseError(response.text)
        return response.json()
    def parse_llm_response(self, data: Dict) -> LLMResponse:
        try:
            content = data["choices"][0]["message"]["content"]
            tokens = data["usage"]["total_tokens"]
            return LLMResponse(
                content=content,
                total_tokens=tokens,
            )
        except KeyError:
            raise APIResponseError("Unexpected response format")
    
    async def generate(self, prompt: str, temperature: float = 0.7,) -> LLMResponse:
        request_model = LLMRequest( prompt=prompt,temperature=temperature,)
        payload = {
            "model": self.settings.model,
            "messages": [{"role": "user", "content": request_model.prompt}],
            "temperature": request_model.temperature,
        }
        raw_data = await self.make_request(payload)
        return self.parse_llm_response(raw_data)