from typing import Set
from backend.core import run_llm
import streamlit as st
from streamlit_chat import message

st.header("LangChain Documentation Assistant")

prompt = st.text_input("Prompt: ", placeholder="Ask me anything about LangChain")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


# nice formatting of URLs for sources
def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


if prompt:
    with st.spinner("Thinking..."):
        generated_response = run_llm(query=prompt)
        # to remove duplicated links
        sources = set(
            [doc.metadata["source"] for doc in generated_response["source_documents"]
        ])
        formatted_sources = (
            f"{generated_response['result']} \n\n Sources: {create_sources_string(sources)}"
        )

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_history"].append(
            formatted_sources
        )

if st.session_state["chat_history"]:
    for index, (generated_response, user_query) in enumerate(
        zip(st.session_state["chat_history"], st.session_state["user_prompt_history"])
    ):
        message(user_query, is_user=True, key=f"user_{index}")
        message(generated_response, is_user=False, key=f"bot_{index}")


