from flask import Flask, url_for
import sqlite3
from random import shuffle

app = Flask(__name__)


@app.route('/')
def mission():
    return ''


@app.route('/scrooll_page')
def image_mars():
    conn = sqlite3.connect('db/generation.db')
    cursor = conn.cursor()
    cursor.execute("""
            SELECT generation_text, author, comment, time FROM all_generation;
            """)
    conn.commit()
    generations = cursor.fetchall()
    shuffle(generations)
    conn.close()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1 style="margin-left: 25px; color: brown">Толстой напился</h1>
    <h2 style="margin-left: 25px">Лента генераций</h2>
    <div>
        <form class="login_form" method="post">
            <div class="form-group">
            <p style="font-size: 28px;">Генерация номер 1</p>
            <p style="font-size: 15px; margin-left: 25px;">author: {generations[0][1]}</p>
            <p style="font-size: 20px; margin-left: 25px;">{generations[0][0]}</p>
            <p style="font-size: 15px; margin-left: 25px;">comment: {generations[0][2]} date: {generations[0][3]}</p>
            <p style="font-size: 28px;">Генерация номер 2</p>
            <p style="font-size: 15px; margin-left: 25px;">author: {generations[1][1]}</p>
            <p style="font-size: 20px; margin-left: 25px;">{generations[1][0]}</p>
            <p style="font-size: 15px; margin-left: 25px;">comment: {generations[1][2]} date: {generations[1][3]}</p>
            <p style="font-size: 28px;">Генерация номер 3</p>
            <p style="font-size: 15px; margin-left: 25px;">author: {generations[2][1]}</p>
            <p style="font-size: 20px; margin-left: 25px;">{generations[2][0]}</p>  
            <p style="font-size: 15px; margin-left: 25px;">comment: {generations[2][2]} date: {generations[2][3]}</p>  
            </div>
        </form>
    </div>
  </body>
</html>"""


if __name__ == '__main__':
    app.run(port=8050, host='127.0.0.1')
