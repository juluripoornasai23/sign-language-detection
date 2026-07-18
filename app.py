import streamlit as st

from rag_model.chat import ask_question


st.set_page_config(
    page_title="Sign Language AI Assistant",
    page_icon="🤟"
)


st.title("🤟 Sign Language AI Assistant")

st.write(
    "Ask questions about Indian Sign Language and get AI-powered answers."
)


question = st.text_input(
    "Enter your question:"
)


if st.button("Ask"):

    if question:

        with st.spinner("Thinking..."):

            answer = ask_question(question)

        st.success("Answer")
        st.write(answer)

    else:
        st.warning("Please enter a question")