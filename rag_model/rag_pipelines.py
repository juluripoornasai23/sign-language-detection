from langchain_google_genai import ChatGoogleGenerativeAI

from .retriever import get_retriever


retriever = get_retriever()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)


def ask(query):

    docs = retriever.invoke(query)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an AI assistant for Sign Language Detection.

Use ONLY the context below.

If the answer is not present,
reply with:
"I don't have information about that sign."

Context:

{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content