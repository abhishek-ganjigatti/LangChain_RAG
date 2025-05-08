from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnableLambda
from langsmith import traceable 
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
langchain_project=os.getenv("LANGCHAIN_PROJECT")

if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
if langchain_project:
    os.environ["LANGCHAIN_PROJECT"] = langchain_project
os.environ["LANGCHAIN_TRACING_V2"] = "true"


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

st.title("LangChain Demo with llama3.2")
input_text = st.text_input("Search the topic you want:")

# Gemini model setup
llm = Ollama(model="llama3.2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


# Handle user input
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
