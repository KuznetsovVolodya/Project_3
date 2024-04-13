from flask import Flask, url_for, render_template, request
from random import choice
from text_creator import a

app = Flask(__name__)




def text_creator(o_t):
    text = o_t
    if len(text) >= 1:
        for i in range(10):
            if text.split()[-1] in a:
                text += ' ' + choice(a[text.split()[-1]])
            else:
                text += ' ' + choice(list(a.keys()))
    return text


@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')


@app.route('/gen', methods=['POST', 'GET'])
def generate():
    gen_text = ""
    if request.method == 'POST':
        gen_text = request.form['about']
    return render_template('gen.html', text=text_creator(gen_text))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
