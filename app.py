import streamlit as st

from utils import get_llm_response
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


st.title("Chat with a virtual assistant", anchor=False)
st.header("Ask a question", anchor=False, divider=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


user_input = st.chat_input("Ask anything about this document")
if user_input:
    response = get_llm_response(user_input)
    with st.chat_message("Assistant"):
        st.write(response)

