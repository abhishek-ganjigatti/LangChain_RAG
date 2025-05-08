# app.py

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env
load_dotenv()

# Set API keys from environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
langchain_project=os.getenv("LANGCHAIN_PROJECT")
if google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key
if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
if langchain_project:
    os.environ["LANGCHAIN_PROJECT"] = langchain_project
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title("LangChain Demo with Gemini API")
input_text = st.text_input("Search the topic you want:")

# Gemini model setup
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Handle user input
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
