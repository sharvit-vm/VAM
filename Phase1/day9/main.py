import asyncio
import json
from ingestion.pipeline import ingest_documents
async def main():
    documents = await ingest_documents("documents")

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(
            [doc.model_dump() for doc in documents],
            f,
            indent=4
        )
    print(f"Ingested {len(documents)} documents")
if __name__ == "__main__":
    asyncio.run(main())