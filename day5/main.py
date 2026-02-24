from models import DocumentInput, ProcessingConfig, ExtractionResult
doc = DocumentInput(
    filename="future_ai.txt",
    content="Artificial Intelligence is reshaping industries and automating processes worldwide.",
    author="Sharvit"
)
print("Word Count:", doc.word_count)
config = ProcessingConfig(
    extract_keywords=True,
    max_keywords=3,
    summary_length=80,
    language="en"
)
summary = doc.content[:config.summary_length]

keywords = [
    {"word": "Artificial Intelligence", "score": 0.95},
    {"word": "industries", "score": 0.88},
    {"word": "automation", "score": 0.90}
]
result = ExtractionResult(
    filename=doc.filename,
    summary=summary,
    keywords=keywords
)
print("\nAverage Keyword Score:", result.average_score)
print("\nSerialized JSON:")
print(result.model_dump_json(indent=2))