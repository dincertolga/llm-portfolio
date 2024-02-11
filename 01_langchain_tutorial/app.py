# Q&A Chatbot
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os

#Function to load openAI model and get response

def get_openai_response(question):
    llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), temperature = 0.5)
    response = llm(question)
    return response

# initialize streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input:  ", key=input)
response = get_openai_response(input)

submit = st.button("Ask the question")

#If ask button is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)
    
