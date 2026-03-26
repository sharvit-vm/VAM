from main import run_pipeline
def test_rag_pipeline_basic():
    file_path = "data/sample.pdf"
    query = "Summarize this document"

    response = run_pipeline(file_path, query)

    assert response is not None
    assert hasattr(response, "answer")
    assert hasattr(response, "sources")
    assert isinstance(response.sources, list)