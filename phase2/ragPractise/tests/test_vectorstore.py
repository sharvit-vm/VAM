from loaders.document_loader import load_document
from splitters.text_splitter import split_documents
from embeddings.embedding_model import get_embeddings
from vectorstore.vector_store import create_vector_store, create_retriever
def test_vectorstore_creation():
    docs = load_document("data/sample.pdf")
    chunks = split_documents(docs)
    embeddings = get_embeddings()
    vectorstore = create_vector_store(chunks, embeddings)

    assert vectorstore is not None
def test_retriever():
    docs = load_document("data/sample.pdf")
    chunks = split_documents(docs)
    embeddings = get_embeddings()
    vectorstore = create_vector_store(chunks, embeddings)
    retriever = create_retriever(vectorstore)

    results = retriever.invoke("What is this about?")

    assert len(results) > 0