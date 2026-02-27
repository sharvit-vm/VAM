import time
import asyncio
import httpx
from typing import List, Dict
from pydantic import BaseModel, model_validator
URLS = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
]

class APIResult(BaseModel):
    url: str
    origin: str
    status_code: int

class CombinedResponse(BaseModel):
    results: List[APIResult]
    @model_validator(mode="after")
    def validate_not_empty(self):
        if not self.results:
            raise ValueError("Results should not be empty")
        return self

#SYNC
def fetch_sync(url: str) -> Dict:
    response = httpx.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "url": data["url"],
        "origin": data["origin"],
        "status_code": response.status_code,
    }
def run_sync():
    start = time.time()
    responses = []

    for url in URLS:
        try:
            responses.append(fetch_sync(url))
        except httpx.HTTPStatusError as e:
            print(f"Error for {url}: {e.response.status_code}")
            responses.append({
                "url": url,
                "origin": None,
                "status_code": e.response.status_code,
            })
    model = CombinedResponse(
        results=[APIResult(**data) for data in responses]
    )
    end = time.time()
    print("\nSYNC VERSION")
    print(model.model_dump_json(indent=2))
    print(f"Sync Execution Time: {end - start:.2f} seconds")

#ASYNC 
async def fetch_async(client: httpx.AsyncClient, url: str) -> Dict:
    response = await client.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "url": data["url"],
        "origin": data["origin"],
        "status_code": response.status_code,
    }
async def run_async():
    start = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [fetch_async(client, url) for url in URLS]
        responses = await asyncio.gather(*tasks)
    model = CombinedResponse(
        results=[APIResult(**data) for data in responses]
    )
    end = time.time()
    print("\nASYNC VERSION")
    print(model.model_dump_json(indent=2))
    print(f"Async Execution Time: {end - start:.2f} seconds")

if __name__ == "__main__":
    run_sync()
    asyncio.run(run_async())


 def show(*args): 
    print(args)

show(1,2,3)