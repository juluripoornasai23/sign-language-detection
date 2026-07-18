import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS

from .embedder import get_embedder


KNOWLEDGE_FOLDER = "knowledge"
DB_FOLDER = "models/faiss_db"


def load_knowledge():

    documents = []

    for file in os.listdir(KNOWLEDGE_FOLDER):
        if file.endswith(".md"):
            loader = TextLoader(
                os.path.join(KNOWLEDGE_FOLDER, file),
                encoding="utf-8"
            )
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    embeddings = get_embedder()

    db = FAISS.from_documents(chunks, embeddings)

    db.save_local(DB_FOLDER)

    print("✅ Knowledge Base Created Successfully!")

    return db


if __name__ == "__main__":
    load_knowledge()