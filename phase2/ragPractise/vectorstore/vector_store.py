from langchain_chroma import Chroma
PERSIST_DIRECTORY = "chroma_db"

def create_vector_store(chunks, embeddings):
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )
    return vectorstore

def load_vector_store(embeddings):
    return Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )

def create_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10
        }
    )