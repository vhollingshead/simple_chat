import streamlit as st
from openai import OpenAI
import os

# Set your OpenAI API key

f = open("/Users/victoriahollingshead/Documents/00_UC_Berkeley_MIDS/CMA/cma_app/apikey.txt", "r")
API_KEY=f.readline()
f.close()

#The OpenAI Key
os.environ['OPENAI_API_KEY'] =API_KEY
client = OpenAI()

# Function to get a response from GPT-3.5 Turbo
def get_gpt3_response(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ])
    return response.choices[0].message.content

# Streamlit app
st.title("GPT-3.5 Turbo Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for chat in st.session_state.chat_history:
    st.write(f"**User:** {chat['user']}")
    st.write(f"**Chatbot:** {chat['chatbot']}")

# Input for the user's message
user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        response = get_gpt3_response(user_input)
        st.session_state.chat_history.append({"user": user_input, "chatbot": response})
        st.write(f"**You:** {user_input}")
        st.write(f"**Chatbot:** {response}")

