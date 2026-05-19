import streamlit as st
from ai_engine import SimpleAI  

st.set_page_config(page_title="ゆうきのAIチャット", layout="centered")

# --- CSS（ChatGPT風） ---
st.markdown("""
<style>

/* 全体の背景（白テーマ） */
[data-testid="stAppViewContainer"] {
    background-color: #ffffff;
    color: #2d2d2d;
}

/* チャット全体の幅を中央に寄せる */
.main {
    max-width: 750px;
    margin: auto;
}

/* --- アニメーション定義（ふわっと出る） --- */
@keyframes fadeInUp {
    0% {
        opacity: 0;
        transform: translateY(8px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/* --- ユーザー吹き出し --- */
[data-testid="stChatMessageUser"] {
    background-color: #e7f3ff;
    border-radius: 12px;
    padding: 12px 16px;
    margin: 8px 0;
    border: 1px solid #c9ddf5;
    color: #2d2d2d;
    box-shadow: 0px 1px 2px rgba(0,0,0,0.08);


    animation: fadeInUp 0.25s ease-out;
}

/* --- AI吹き出し --- */
[data-testid="stChatMessageAssistant"] {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 12px 16px;
    margin: 8px 0;
    border: 1px solid #e5e5e5;
    color: #2d2d2d;
    box-shadow: 0px 1px 2px rgba(0,0,0,0.08);

    /* ふわっとアニメーション */
    animation: fadeInUp 0.25s ease-out;
}

/* 吹き出し内のテキスト */
[data-testid="stChatMessageUser"] p,
[data-testid="stChatMessageAssistant"] p {
    font-size: 16px;
    line-height: 1.6;
}

/* 入力欄 */
[data-testid="stChatInput"] {
    background-color: #ffffff;
    color: #2d2d2d;
    border-radius: 10px;
}

textarea {
    background-color: #ffffff !important;
    color: #2d2d2d !important;
    border-radius: 10px !important;
    border: 1px solid #cccccc !important;
}

</style>
""", unsafe_allow_html=True)



# --- AI インスタンス ---
if "ai" not in st.session_state:
    st.session_state.ai = SimpleAI()

# --- チャット履歴 ---
if "chat" not in st.session_state:
    st.session_state.chat = []

st.title("ゆうきのAIチャット")

# --- チャット表示 ---
for msg in st.session_state.chat:
    st.chat_message(msg["role"]).write(msg["content"])

# --- 入力欄 ---
user_input = st.chat_input("メッセージを入力してAIと会話しましょう")

if user_input:
    # ユーザーの発言を表示
    st.session_state.chat.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    #ai_engineで返答生成
    ai_reply = st.session_state.ai.respond(user_input)

    # AI の返答を表示
    st.session_state.chat.append({"role": "assistant", "content": ai_reply})
    st.chat_message("assistant").write(ai_reply)
