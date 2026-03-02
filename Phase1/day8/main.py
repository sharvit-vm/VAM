import asyncio
from app.client import AsyncLLMClient
async def main():
    client = AsyncLLMClient()
    response = await client.generate(
        "Explain async programming in simple words."
    )
    print("\nResponse:")
    print(response.content)
    print("\nTokens used:", response.total_tokens)
if __name__ == "__main__":
    asyncio.run(main())