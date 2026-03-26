from loaders.document_loader import load_document
from splitters.text_splitter import split_documents
def test_loader():
    docs = load_document("data/sample.pdf")
    assert docs is not None
    assert len(docs) > 0

def test_splitter():
    docs = load_document("data/sample.pdf")
    chunks = split_documents(docs)

    assert chunks is not None
    assert len(chunks) > 0