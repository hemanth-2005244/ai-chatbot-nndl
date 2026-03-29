import streamlit as st
import time

st.set_page_config(page_title="AI Chatbot", layout="centered")

# -------------------------
# 🎨 ULTRA MODERN CSS
# -------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #00f5ff;
    text-shadow: 0px 0px 30px #00f5ff;
}

/* Chat container */
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* Glass effect */
.user, .bot {
    backdrop-filter: blur(10px);
    padding: 12px;
    border-radius: 15px;
    max-width: 70%;
}

/* User bubble */
.user {
    align-self: flex-end;
    background: rgba(56, 189, 248, 0.2);
    border: 1px solid #38bdf8;
    text-align: right;
}

/* Bot bubble */
.bot {
    align-self: flex-start;
    background: rgba(34, 197, 94, 0.2);
    border: 1px solid #22c55e;
}

/* Input box */
input {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 🧠 Chat memory
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# 🤖 Chatbot logic
# -------------------------
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

# -------------------------
# 🖥 UI Header
# -------------------------
st.markdown('<div class="title">🤖 Neural AI Chatbot</div>', unsafe_allow_html=True)
st.caption("⚡ Deep Learning | NLP | Engineering Project")

# -------------------------
# 💬 Display chat
# -------------------------
for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f'<div class="user">👨‍💻 {msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot">🤖 {msg}</div>', unsafe_allow_html=True)

# -------------------------
# ⌨️ Input + Button
# -------------------------
col1, col2 = st.columns([4,1])

with col1:
    user_input = st.text_input("Type message...", key="input")

with col2:
    send = st.button("Send 🚀")

# -------------------------
# ⚡ Handle input
# -------------------------
if send and user_input:
    st.session_state.messages.append(("user", user_input))

    # Typing effect
    with st.spinner("🤖 Bot is typing..."):
        time.sleep(1)
        response = chatbot_reply(user_input)

    st.session_state.messages.append(("bot", response))

    st.rerun()
