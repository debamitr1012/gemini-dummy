import streamlit as st
import os
import google.generativeai as genai

st.title("Chat - Gemini Bot")
# Set Google API key
os.environ['GOOGLE_API_KEY'] = "Your Google API Key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
# Create the Model
model = genai.GenerativeModel('gemini-pro')
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content":"Ask me Anything"
        }
    ]
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    st.write(f"{message['role']}: {message['content']}")
# Process and store Query and Response
def llm_function(query):
    response = model.generate_content(query)
    # Displaying the Assistant Message
    st.write(f"assistant: {response.text}")
    # Storing the User Message
    st.session_state.messages.append(
        {
            "role":"user",
            "content": query
        }
    )
    # Storing the User Message
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content": response.text
        }
    )
# Accept user input
query = st.text_input("What is up?")
# Calling the Function when Input is Provided
if query:
    llm_function(query)
