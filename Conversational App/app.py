import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import HuggingFaceHub

load_dotenv()
import os
os.environ["HUGGINGFACE_API_KEY"]=os.getenv("HUGGINGFACE_API_KEY")
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
st.set_page_config(page_title="LangChain Chat",page_icon=":robot")
st.header("Hey,I'm your ChatBot")
if "sessionMessages" not in st.session_state:
     st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]



def load_answer(question):

    st.session_state.sessionMessages.append(HumanMessage(content=question))

    assistant_answer  = chat.invoke(st.session_state.sessionMessages )

    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))

    return assistant_answer.content


def get_text():
    input_text = st.text_input("You: ")
    return input_text


chat = model_kwargs={"temperature":0.5, 'max_new_tokens':250}




user_input=get_text()
submit = st.button('Generate')  

if submit:
    
    response = load_answer(user_input)
    st.subheader("Answer:")

    st.write(response)

