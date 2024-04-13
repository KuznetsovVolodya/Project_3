from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')


@app.route('/gen', methods=['POST', 'GET'])
def generate():
    gen_text = ""
    if request.method == 'POST':
        gen_text = request.form['about'] + 'a'
    return render_template('gen.html', text=gen_text)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
