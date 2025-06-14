import streamlit as st
import openai
###############################################################################
# チャットボットとやりとりする関数
###############################################################################
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.3
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去
###############################################################################
# Streamlitの「Secrets」からOpenAI API keyを取得
###############################################################################
openai.api_key = st.secrets.OpenAIAPI.openai_api_key
###############################################################################
# システムプロンプトの定義
###############################################################################
system_prompt = """
あなたは優秀なプログラミング講師です。
プログラミング上達のために、生徒のレベルに合わせて適切なアドバイスを行ってください。
あなたの役割は生徒のプログラミングスキルを向上させることなので、
例えば以下のようなプログラミング以外のことを聞かれても、絶対に答えないでください。

* 旅行
* 料理
* 芸能人
* 映画
* 科学
* 歴史
"""
###############################################################################
# st.session_stateを使いメッセージを保存
###############################################################################
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": system_prompt}
    ]
###############################################################################
# ユーザーインターフェイスの構築
###############################################################################
st.title(" 「プログラミング講師」ボット")
st.write("プログラミングに関して、何でも聞いてください。")
user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]
    for message in reversed(messages[1:]):  # システムプロンプト以外を直近のメッセージを上にして表示
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])

###############################################################################
# メッセージの構成
###############################################################################
#    st.session_state["messages"] = [
#        {"role": "system",    "content": "システムプロンプト"},
#        {"role": "user",      "content": "ユーザプロンプト(1回目)"},
#        {"role": "assistant", "content": "アシスタント回答(1回目)"},
#        {"role": "user",      "content": "ユーザプロンプト(2回目)"},
#        {"role": "assistant", "content": "アシスタント回答(2回目)"},
#                                  ・
#                                  ・
#                                  ・
#        {"role": "user",      "content": "ユーザプロンプト(n回目)"},
#        {"role": "assistant", "content": "アシスタント回答(n回目)"}
#    ]
# ★注意★"system"を指定できないモデルも存在する。
###############################################################################
# temperature パラメータの概要
###############################################################################
# OpenAI APIのChatCompletion.createメソッドにおける重要なパラメータの一つで、
# モデルが生成するテキストのランダム性（多様性、創造性）を制御するために使用されます。
# temperature は、0から2までの浮動小数点数で指定されます
# （モデルやAPIのバージョンによって範囲が異なる場合がありますが、一般的にはこの範囲です）。
# 値が低いほど（0に近づくほど）、モデルはより確定的で、論理的、保守的なテキストを生成します。
# 値が高いほど（2に近づくほど）、モデルはより多様で、創造的、予測不能なテキストを生成します。
# ★注意★temperatureを指定できないモデルも存在する。


