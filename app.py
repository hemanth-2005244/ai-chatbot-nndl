print("🔥 RUNNING THIS APP.PY FILE 🔥")
import streamlit as st
import numpy as np
import pickle
import re
if "messages" not in st.session_state:
    st.session_state.messages = []
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #00f5ff;
    text-shadow: 0px 0px 25px #00f5ff;
    margin-bottom: 10px;
}

/* Chat container */
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* User bubble */
.user-bubble {
    align-self: flex-end;
    background: linear-gradient(135deg, #38bdf8, #0ea5e9);
    color: white;
    padding: 10px 15px;
    border-radius: 15px;
    max-width: 70%;
    box-shadow: 0 0 10px #38bdf8;
}

/* Bot bubble */
.bot-bubble {
    align-self: flex-start;
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    padding: 10px 15px;
    border-radius: 15px;
    max-width: 70%;
    box-shadow: 0 0 10px #22c55e;
}

/* Input box */
input {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)
print("APP STARTED")  # confirm correct file

# Load model
def chatbot_reply(text):
    text = text.lower()

    if "hi" in text:
        return "hello 👋"
    elif "how are you" in text:
        return "I am fine 😊"
    elif "name" in text:
        return "I am an AI chatbot 🤖"
    elif "bye" in text:
        return "Goodbye 👋"
    else:
        return "I don't understand 😅"

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Get correct input length directly from model
max_len = model.input_shape[1]   # 🔥 AUTO FIX

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def chatbot_reply(text):
    text = text.lower()

    seq = tokenizer.texts_to_sequences([text])[0]

    # 🔥 FORCE LENGTH FROM MODEL
    max_len = model.input_shape[1]

    seq = seq[:max_len]
    while len(seq) < max_len:
        seq.append(0)

    seq = np.array([seq])

    print("FINAL SHAPE:", seq.shape)

    pred = model.predict(seq, verbose=0)
    word_id = np.argmax(pred)

    return tokenizer.index_word.get(word_id, "I don't understand")

# Title
st.markdown('<div class="title">🤖 Neural AI Chatbot</div>', unsafe_allow_html=True)
st.caption("⚡ Deep Learning | NLP | LSTM Powered")

# Input
user_input = st.text_input("💬 Ask something...")

if user_input:
    response = chatbot_reply(user_input)

    # Store chat
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "bot", "content": response})
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">👨‍💻 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">🤖 {msg["content"]}</div>', unsafe_allow_html=True)
