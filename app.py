import streamlit as st
from ai_engine import SimpleAI

st.set_page_config(page_title="AI Chat Demo", page_icon="🤖")

ai = SimpleAI()

st.title("ゆうきのAIチャット")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("メッセージを入力")

if user_input:
    ai_response = ai.respond(user_input)
    st.session_state.chat.append(("あなた", user_input))
    st.session_state.chat.append(("AI", ai_response))

for role, msg in st.session_state.chat:
    with st.chat_message("user" if role == "あなた" else "assistant"):
        st.markdown(msg)

