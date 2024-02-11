import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os


def get_llm_response(num_facts, topic):
    
    # calling llama model
    llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), temperature = 0.5)
    
    # prompt template
    template = """ Give me {num_facts} fun facts about {topic}. """
    
    prompt = PromptTemplate(input_variables =["num_facts","topic"],
                            template = template)
    
    # generate response from llama-2
    response = llm(prompt.format(num_facts = num_facts,topic=topic))
    
    print(response)
    return response


st.set_page_config(page_title = "Fun Facts", 
                   layout = "centered", 
                   initial_sidebar_state = "collapsed")

st.header('Fun Facts')

topic = st.text_input("Enter the topic")

# create two more columns for additional fields
col1,col2 = st.columns([5,5])

with col1:
    num_facts= st.text_input("Number of Facts")

submit = st.button("Generate")

# final response

if submit:
    st.write(get_llm_response(num_facts, topic))


