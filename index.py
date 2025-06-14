import streamlit as st
import re

st.title("＜発表内容＞")

try:
    with open('全体構成.txt', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    content = '全体構成.txt が見つかりません。'

# マークダウンとして表示（preやcodeブロックは使わない）
st.markdown(content)