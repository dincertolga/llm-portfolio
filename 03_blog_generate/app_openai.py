import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os

def get_llm_response(input_text, num_words, blog_style):
    
    # calling llama model
    llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), temperature = 0.5)
    # prompt template
    
    template = """ Write a blog for {blog_style} job profie for the topic {input_text} within {num_words} words. """
    
    prompt = PromptTemplate(input_variables =["blog_style","input_text","num_words"],
                            template = template)
    
    # generate response from openai
    response = llm(prompt.format(blog_style = blog_style,input_text=input_text, num_words= num_words))
    
    print(response)
    return response


st.set_page_config(page_title = "Generate a Blog", 
                   layout = "centered", 
                   initial_sidebar_state = "collapsed")

st.header('Generate Blogs')

input_text = st.text_input("Enter the blog topic")

# create two more columns for additional fields
col1,col2 = st.columns([5,5])

with col1:
    num_words= st.text_input("Number of Words")
with col2:
    blog_style = st.selectbox('Writing the blog for', 
                              ('Researchers', 'Data Scientists', 'Common People'), index = 0)
submit = st.button("Generate")

# final response

if submit:
    st.write(get_llm_response(input_text, num_words, blog_style))


