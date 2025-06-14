from flask import Flask, render_template_string
import re

app = Flask(__name__)

def linkify(text):
    # URLを検出してリンクに変換
    url_pattern = re.compile(r'(https?://[^\s]+)')
    return url_pattern.sub(r'<a href="\1" target="_blank">\1</a>', text)

@app.route('/')
def show_txt():
    try:
        with open('全体構成.txt', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = '全体構成.txt が見つかりません。'
    content = linkify(content)
    return render_template_string("""
    <h1>全体構成.txt の内容</h1>
    <pre style="background:#eee; padding:1em; white-space: pre-wrap;">{{ content|safe }}</pre>
    """, content=content)

if __name__ == '__main__':
    app.run(port=5002, debug=False)