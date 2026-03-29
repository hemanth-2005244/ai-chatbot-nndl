import streamlit as st

st.set_page_config(page_title="AI Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Simple chatbot logic (NO TensorFlow)
def chatbot_reply(text):
    text = text.lower()

    if "hi" in text:
        return "Hello 👋"
    elif "how are you" in text:
        return "I am fine 😊"
    elif "name" in text:
        return "I am an AI chatbot 🤖"
    elif "bye" in text:
        return "Goodbye 👋"
    else:
        return "I don't understand 😅"

# UI
st.title("🤖 AI Chatbot")

user_input = st.text_input("Type your message:")

if user_input:
    response = chatbot_reply(user_input)

    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Display chat
for sender, msg in st.session_state.messages:
    st.write(f"{sender}: {msg}")
