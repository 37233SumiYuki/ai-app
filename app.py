import streamlit as st
from ai_engine import SimpleAI  

# --- ページ設定 ---
st.set_page_config(page_title="ゆうきのAIチャット", layout="centered")

# --- CSS ---
st.markdown("""
<style>

/* 背景 */
[data-testid="stAppViewContainer"] {
    background-color: #ffffff;
    color: #000000;
}

/* 中央に寄せる */
.main {
    max-width: 750px;
    margin: auto;
}

/* アニメーション */
@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(8px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* 吹き出し(ユーザー) */
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

/* 吹き出し（AI) */
[data-testid="stChatMessageAssistant"] {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 12px 16px;
    margin: 8px 0;
    border: 1px solid #e5e5e5;
    color: #2d2d2d;
    box-shadow: 0px 1px 2px rgba(0,0,0,0.08);
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

# --- 会話リセット ---
with st.sidebar:
    if st.button("会話をリセット"):
        st.session_state.chat = []
        st.session_state.ai = SimpleAI()
        st.rerun()

# --- AIインスタンスの初期化 ---
if "ai" not in st.session_state:
    st.session_state.ai = SimpleAI()

# --- チャット履歴の初期化 ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- タイトル ---
st.title("ゆうきのAIチャット")

# --- 履歴の表示 ---
for msg in st.session_state.chat:
    st.chat_message(msg["role"]).write(msg["content"])

# --- メッセージ入力欄 ---
user_input = st.chat_input("メッセージを入力してAIと会話しましょう")

if user_input:
    # ユーザーの発言を履歴に追加
    st.session_state.chat.append({"role": "user", "content": user_input})

    # AI返答の生成
    try:
        with st.spinner("考え中..."):
            ai_reply = st.session_state.ai.respond(user_input, history=st.session_state.chat)
    except Exception as e:
        ai_reply = f"エラーが発生しました: {e}"

    # AIの返答を履歴に追加して再描画
    st.session_state.chat.append({"role": "assistant", "content": ai_reply})
    st.rerun()
