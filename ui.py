import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="PDF RAG Chatbot", page_icon="🤖")
st.title("🤖 Knowledge-Based Chatbot")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything about the PDF..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        with st.spinner("Thinking..."):
            response = requests.post(API_URL, json={"question": prompt})
            
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
            else:
                answer = f"Error: {response.status_code} - {response.text}"

    
        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        st.error(f"Could not connect to backend: {e}")