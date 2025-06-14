import streamlit as st
import re

st.title("＜発表内容＞")

try:
    with open('全体構成.txt', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    content = '全体構成.txt が見つかりません。'

def linkify(text):
    # URLを検出してマークダウンリンクに変換
    url_pattern = re.compile(r'(https?://[^\s\)\]]+)')
    return url_pattern.sub(r'[\1](\1)', text)

content = linkify(content)

# マークダウンとして表示（preやcodeブロックは使わない）
st.markdown(content)