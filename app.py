import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAV9Y1QS_uw2HPeWxMmtiR-SXuamvVKe1w")


## function to load Gemini Pro model and get responses

model=genai.GenerativeModel("gemini-1.5-flash")
print(model)
def get_gemini_responses(question):
    response = model.generate_content(question)
    print(response)
    print("-------------------------role...................", response.parts)
    return response.text

    ##initialize  our streamlit app

st.header("Gemini LLM Application")

input = st.text_input("Input:", key="input")
submit = st.button("Ask The Question")

##When submit is clicked 

if submit:
    response = get_gemini_responses(input)
    st.subheader("The Response is")
    st.write(response)

        
