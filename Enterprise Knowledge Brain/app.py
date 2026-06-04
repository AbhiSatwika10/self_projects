import streamlit as st
import requests

st.set_page_config(page_title="Enterprise Knowledge Brain")

st.title("Enterprise Knowledge Brain (Agentic RAG)")

query = st.text_input("Ask Enterprise Knowledge Questions")

if st.button("Ask"):
    response = requests.get(
        f"http://localhost:8000/ask?query={query}"
    )

    st.write(response.json()["response"])
