import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import utils.rag_utils as rag_utils
import utils.web_search as web_search

st.set_page_config(page_title="AI Knowledge Assistant", page_icon="🤖")

st.title("AI Knowledge Assistant Chatbot")

mode = st.sidebar.radio(
    "Response Mode",
    ["Concise", "Detailed"]
)

if "vector_db" not in st.session_state:
    st.session_state.vector_db = rag_utils.build_vector_database()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    context = rag_utils.retrieve_context(prompt, st.session_state.vector_db)
    web_results = web_search.search_web(prompt)

    if mode == "Concise":
        response = f"Short answer based on context:\n\n{context}\n\nWeb info:\n{web_results}"
    else:
        response = f"Detailed explanation based on context:\n\n{context}\n\nWeb info:\n{web_results}"

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
