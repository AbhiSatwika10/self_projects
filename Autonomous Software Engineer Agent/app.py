import streamlit as st
import requests

st.set_page_config(page_title="Autonomous Software Engineer Agent")

st.title("Autonomous Software Engineer Agent")

task = st.text_area("Enter Engineering Task")

if st.button("Execute Task"):

    response = requests.post(
        "http://localhost:8000/execute",
        json={"prompt": task}
    )

    st.json(response.json())
