from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from rag.pdf_loader import load_pdf

retriever = None


def load_vectorstore(pdf_path):

    global retriever

    chunks = load_pdf(pdf_path)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    retriever = vectorstore.as_retriever()