import streamlit as st
from utils.rag_utils import load_documents, retrieve_context
from utils.web_search import search_web

st.set_page_config(page_title="AI Knowledge Assistant")

st.title("AI Knowledge Assistant Chatbot")

mode = st.sidebar.radio(
    "Response Mode",
    ["Concise", "Detailed"]
)

if "docs_loaded" not in st.session_state:
    load_documents()
    st.session_state.docs_loaded = True

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

    context = retrieve_context(prompt)
    web_results = search_web(prompt)

    if mode == "Concise":
        response = f"{context}\n\n{web_results}"
    else:
        response = f"""
    Answer based on document knowledge:

    {context}

    Additional information from web search:

    {web_results}
    """

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
