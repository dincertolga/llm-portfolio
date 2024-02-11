import streamlit as st
import os
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

#from dotenv import load_dotenv
#load_dotenv()
import os

def get_openai_response(question):
    llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), temperature = 0.5)
    response = llm(question)
    return response


# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    response = get_openai_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    
    #for chunk in response:
    st.write(response)
    st.session_state['chat_history'].append(("Bot", response))
st.subheader("The Chat History is")
    
for role, texts in st.session_state['chat_history']:
    st.write(f"{role}: {texts}")
    