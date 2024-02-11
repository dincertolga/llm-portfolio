import streamlit as st
import os
import sqlite3

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

os.environ["OPENAI_API_KEY"] = ""

def get_llm_response(question):
    
    llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), temperature = 0.5)
    # prompt template
    
    template = """ You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output. You can use synonyms for words, for example: grades = MARKS etc.
    % question
    {question}

    YOUR RESPONSE:
    """
    
    prompt = PromptTemplate(input_variables =["question"],
                            template = template)
    
    # generate response from openai
    response = llm(prompt.format(question = question))
    
    print(response)
    return response

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


## Streamlit App

st.set_page_config(page_title="Retrieve Any SQL query")
st.header("App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_llm_response(question)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)