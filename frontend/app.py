import streamlit as st
import requests

st.title("Ask LLM")

prompt = st.text_area("Enter your prompt:")

if st.button("Ask LLM"):
    if prompt.strip():
        response = requests.post(
            "http://backend:8000/ask_llm",  # Use backend service name for Docker Compose
            json={"prompt": prompt}
        )
        if response.ok:
            st.write(response.json()["response"])
        else:
            st.error("Error: Could not get response from backend.")
    else:
        st.warning("Please enter a prompt.")
