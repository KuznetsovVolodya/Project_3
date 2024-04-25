import sqlite3
from flask import Flask, render_template, request, redirect
from random import choice, shuffle

from text_creator import a
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from data.users import User
from data import db_session
from fish_api_connection import gen_prof

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def text_creator(o_t):
    text = o_t
    if len(text) >= 1:
        for i in range(10):
            if text.split()[-1] in a:
                text += ' ' + choice(a[text.split()[-1]])
            else:
                text += ' ' + choice(list(a.keys()))
    return text


def text_creator_prof(o_t):
    return o_t + " " + gen_prof()


class RegisterForm(FlaskForm):
    username = StringField('Ник', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    username = StringField('Ник', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
@app.route('/scrooll_page/<username>/<post>')
def image_mars2(username, post):
    conn = sqlite3.connect('db/generation1.db')
    cursor = conn.cursor()
    cursor.execute("""
            SELECT generation_text, author, comment, time FROM all_generation;
            """)
    conn.commit()
    generations = cursor.fetchall()
    shuffle(generations)
    conn.close()

    return render_template('scroll.html', enter=username)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.name == form.username.data).first():
            return render_template('form_enter.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.username.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect(f'/index/{form.username.data}')
    return render_template('form_enter.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.name == form.username.data).first()
        if user and user.check_password(form.password.data):
            return redirect(f'/index/{form.username.data}')
        return render_template('form_enter.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('form_enter.html', title='Авторизация', form=form)


@app.route('/index/<username>')
def index_entered(username):
    return render_template('main.html', enter=username)


@app.route('/gen/<username>', methods=['POST', 'GET'])
def generate_entered(username):
    gen_text = ""
    if request.method == 'POST':
        gen_text = request.form['about']
    return render_template('gen.html', name="Вторая степень опьянения", enter=username,
                           description='Полный бред, где хоть какую-то связь можно проследить только между соседними '
                                       'словами.',
                           message='!Пиши строчными буквами и без знаков препинания!', text=text_creator(gen_text))


@app.route('/gen_prof/<username>', methods=['POST', 'GET'])
def generate_prof_entered(username):
    gen_text = ""
    if request.method == 'POST':
        gen_text = request.form['about']
        gen_text = text_creator_prof(gen_text)
    return render_template('gen.html', name="Первая степень опьянения", enter=username,
                           description='На первый взгляд текст выглядит логично, но стоит вчитаться, как вы сразу '
                                       'поймёте его абсурдность.',
                           message='!Ничего вводить не нужно, генерация производится сама!',
                           text=gen_text)


if __name__ == '__main__':
    db_session.global_init("db/new_generation.db")
    user = User()
    db_sess = db_session.create_session()
    user.name = "<Борис>"
    user.set_password("GLAGOL")
    db_sess.add(user)
    user2 = User()
    user2.name = "Андрей"
    user.set_password("Privet")
    db_sess.add(user2)
    db_sess.commit()

    app.run(port=8080, host='127.0.0.1')
