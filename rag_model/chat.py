import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from .retriever import get_retriever


load_dotenv()


def ask_question(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )

    prompt = f"""
You are a helpful Indian Sign Language assistant.

Answer the question using only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":

    question = "What is Indian Sign Language?"

    answer = ask_question(question)

    print("\nAssistant:")
    print(answer)