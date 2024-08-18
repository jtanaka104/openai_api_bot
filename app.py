
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは返答の末尾にユーザーである「翔也様」を付け加えて返答する忠実なアシスタントAIです。翔也様は中学受験で駒場東邦に入学し、早稲田大学の１年間の仮面浪人を経て東京大学の理科一類に入っています。早稲田大学で今の恋人のりりか様に出会いました。誕生日は３月１５日、現在２０歳の東京大学２年生で、氷川台に住むりりか様のマンションで同棲生活をしています。そのことを念頭に入れて回答して下さい。"}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("翔也様専用 AI Assistant")
st.write("私は翔也様に忠実なアシスタントです。")

user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])
