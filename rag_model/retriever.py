import os
from langchain_community.vectorstores import FAISS

from .embedder import get_embedder


DB_FOLDER = "models/faiss_db"


def get_retriever():

    embeddings = get_embedder()

    db = FAISS.load_local(
        DB_FOLDER,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(
        search_kwargs={
            "k": 3
        }
    )

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    results = retriever.invoke(
        "What is Indian Sign Language?"
    )

    for doc in results:
        print("\n---")
        print(doc.page_content)