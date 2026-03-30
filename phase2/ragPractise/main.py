from loaders.document_loader import load_document
from splitters.text_splitter import split_documents
from embeddings.embedding_model import get_embeddings
from vectorstore.vector_store import (create_vector_store,load_vector_store,create_retriever)
from chains.rag_chain import create_rag_chain
from cache.cache import enable_cache
import os
import hashlib
PERSIST_DIRECTORY = "chroma_db"

def get_file_hash(file_path: str) -> str:
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def ingest_data(file_path: str):
    docs = load_document(file_path)
    chunks = split_documents(docs)
    file_hash = get_file_hash(file_path)
    print("File hash created")
    for chunk in chunks:
        chunk.metadata["source"] = file_path
        chunk.metadata["hash"] = file_hash
    embeddings = get_embeddings()
    if os.path.exists(PERSIST_DIRECTORY):
        vectorstore = load_vector_store(embeddings)
        print("Loaded existing vector store")
        existing = vectorstore.get()
        existing_hashes = set()
        for meta in existing.get("metadatas", []):
            if meta and "hash" in meta:
                existing_hashes.add(meta["hash"])

        if file_hash not in existing_hashes:
            vectorstore.add_documents(chunks)
            print("Added new document to vector store")
            return "added"   
        else:
            print("Document already exists, skipping")
            return "skipped" 

    else:
        create_vector_store(chunks, embeddings)
        print("Created new vector store")
        return "created"   
def ask_question(query: str):
    enable_cache()

    embeddings = get_embeddings()
    vectorstore = load_vector_store(embeddings)

    retriever = create_retriever(vectorstore)
    chain = create_rag_chain(retriever)
    response = chain.invoke(query)
    print("\nAnswer:\n", response.answer)
    print("\nSources:\n", response.sources)
    return response
if __name__ == "__main__":
    file_path = "data/sample.pdf"

    #Ingest FIRST (correct sequence)
    ingest_data(file_path)

    # Query loop
    while True:
        query = input("\nAsk a question (type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        ask_question(query)