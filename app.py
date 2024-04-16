from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import sqlite3
import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Function to Load Google Gemini Model

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text


## Function to retrieve query from the database

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows



## Define the Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL code!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION \n\n For example, \nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Computer Science class?,
    the SQL command will be something like this SELECT FROM STUDENT where CLASS="Computer Science";
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]



## Streamlit App

st.set_page_config("SQL Query Retriever")

st.header("SQL Query Retriever")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the Question")


## If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    response = read_sql_query(response, 'student.db')
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)