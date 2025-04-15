from email import header
from pyexpat import model
from tracemalloc import start
from urllib import response
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
     
genai.configure(api_key=os.getenv("AIzaSyAV9Y1QS_uw2HPeWxMmtiR-SXuamvVKe1w"))

## function to load Gemini pro model and get response
model=genai.GenerativeModel("gemini 2.5 pro preview")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response
    ##initialize our streamlit app
    st.set_page_config(page_title="Q&A Demo")

    st.header("Gemini LLM application")

    if 'chat history' not in st.session_state:
        st.session_state['chat history']=[]

    input=st.text_input("Input:",key="input")
    submit=st.button("ask the question")

    if submit and input:
        response=get_gemini_response(input)

        ## add user query and response to session chat history
        st.session_state['chat history'].append(("you",input))
        st.subheader("the Response is ")
        for chunk in response:
            st.write(chunk.text)
            st.session_stste['chat_history'].append(("bot",chunk.text))
        st.subheader("the chat history is")

        for role,text in st.session_state['chat_history']:
            st.write(f"{role}:{text}")








