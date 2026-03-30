import streamlit as st
import os
from main import ingest_data, ask_question
from embeddings.embedding_model import get_embeddings
from vectorstore.vector_store import load_vector_store, create_retriever
PERSIST_DIRECTORY = "chroma_db"

os.makedirs("data", exist_ok=True)
if "processed_files" not in st.session_state:
    st.session_state.processed_files = set()

if "last_query" not in st.session_state:
    st.session_state.last_query = ""

if "last_response" not in st.session_state:
    st.session_state.last_response = None

@st.cache_resource
def get_vectorstore():
    embeddings = get_embeddings()
    return load_vector_store(embeddings)

st.set_page_config(page_title="RAG Q&A System", layout="wide")

st.title("RAG Document Q&A System")
st.markdown("Upload documents and ask questions based on their content.")

uploaded_files = st.file_uploader(
    "Upload documents",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = f"data/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if file_path not in st.session_state.processed_files:
            with st.spinner(f"Processing {uploaded_file.name}..."):
                status = ingest_data(file_path)
            st.session_state.processed_files.add(file_path)
            if status == "created":
                st.success(f"{uploaded_file.name} → Vector DB created")
            elif status == "added":
                st.success(f"{uploaded_file.name} → Added to vector DB")
            elif status == "skipped":
                st.info(f"{uploaded_file.name} → Already exists (same content)")
        else:
            st.info(f"{uploaded_file.name} already processed in this session")

st.divider()
query = st.text_input("Ask a question", value=st.session_state.last_query)
col1, col2 = st.columns([1, 5])
with col1:
    ask_clicked = st.button("Ask")
if ask_clicked and query:
    st.session_state.last_query = query
    with st.spinner("Generating answer..."):
        response = ask_question(query)
        vectorstore = get_vectorstore()
        retriever = create_retriever(vectorstore)
        docs = retriever.invoke(query)
        sources = list(set([
            doc.metadata.get("source", "")
            for doc in docs if doc.metadata
        ]))
        st.session_state.last_response = {
            "answer": response.answer,
            "sources": sources
        }

if st.session_state.last_response:
    st.subheader("Answer")
    st.write(st.session_state.last_response["answer"])
    st.subheader("Sources")
    sources = st.session_state.last_response["sources"]
    if sources:
        for src in sources:
            st.write(f"- {src}")
    else:
        st.write("No sources found")