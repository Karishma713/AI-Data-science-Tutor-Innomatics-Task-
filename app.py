import streamlit as st
import time
from components.chatbot import get_chatbot, get_response

# 🎨 Streamlit Page Config
st.set_page_config(page_title="AI Data Science Tutor", page_icon="🧠", layout="centered")

# 🌟 Custom CSS for Styling
st.markdown("""
    <style>
        .chat-container {
            background-color: black;  /* Light background for contrast */
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .chat-text {
            font-size: 18px;
            font-weight: bold;
            color: white;  /* Dark text for readability */
        }
    </style>
""", unsafe_allow_html=True)


# 🔥 Header Section
st.title("🧠 AI Data Science Tutor")
st.write("Ask me anything about **Data Science**, and I'll guide you! 📊✨")

# Get chatbot instance
llm, memory = get_chatbot()

# User input section
user_input = st.text_input("💬 Ask your question:")

if user_input:
    # Simulated typing effect ⌨️
    with st.spinner("🤖 Thinking..."):
        time.sleep(1)  # Simulate delay
        tutor_response = get_response(user_input, llm)

    # Display in a styled container
    st.markdown(f"<div class='chat-container'><p class='chat-text'>{tutor_response}</p></div>", unsafe_allow_html=True)

