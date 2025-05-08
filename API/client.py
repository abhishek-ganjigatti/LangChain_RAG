import requests
import streamlit as st

def get_GCP_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})
    return response.json()['output']

def get_Ollama_response(input_text1):
    response=requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})
    return response.json()['output']

st.title('LangChain API varification for Client app')
input_text=st.text_input("Write essay on")
input_text1=st.text_input("Write poem on")

if input_text:
    st.write(get_GCP_response(input_text))
    
if input_text1:
    st.write(get_Ollama_response(input_text))