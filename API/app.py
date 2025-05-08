from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI  # Ensure this import is correct
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableMap

# Load environment variables from .env
load_dotenv()

# Load API key for Google if needed
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key  # Set it for Google Cloud

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Serve static files (e.g., for favicon.ico)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define root route
@app.get("/")
def sdgfnhdsffgfhdd():
    return {"message": "Welcome to  API"}

# Initialize the Google Generative AI model
google_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")  # Specify a model name

# Add route for the Google Generative AI model
add_routes(
    app,
    google_model,
    path="/genai"
)

# Initialize Ollama model
llm = Ollama(model="llama3.2")

# Define your prompt templates
prompt1 = ChatPromptTemplate.from_template("write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("write me a testcase scenerios for {topic} with 20 steps")
essay_chain = prompt1 | google_model 
# Add routes for the essay and poem generation
add_routes(
    app,
    essay_chain,  # Use Google model for essay route
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm,  # Use Ollama model for poem route
    path="/poem"
)

# Start the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
