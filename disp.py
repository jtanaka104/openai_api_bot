from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def show_app_py():
    try:
        with open('app.py', encoding='utf-8') as f:
            code = f.read()
    except FileNotFoundError:
        code = 'app.py が見つかりません。'
    return render_template_string("""
    <h1>app.py の内容</h1>
    <pre style="background:#eee; padding:1em; white-space: pre-wrap;">{{ code }}</pre>
    """, code=code)

if __name__ == '__main__':
    app.run(port=5001, debug=False)