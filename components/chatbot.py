import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from .memory import get_memory

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def get_chatbot():
    """Initialize chatbot with memory support and AI model."""
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7, google_api_key=api_key)
    memory = get_memory()
    return llm, memory

def get_response(user_input, llm):
    """Generate a response from the AI model."""
    response = llm.invoke(user_input)
    
    # Extract response content
    if hasattr(response, "content"):
        return f"🤖 **Tutor:** {response.content} ✨"
    else:
        return "⚠️ Sorry, I couldn't process your request."
