import sqlite3
import os

from flask import Flask, render_template, request, flash, session, redirect, url_for, abort

from DataBase import DataBase

DATABASE = '/tmp/homework.db'
DEBUG = True
SECRET_KEY = "12482rqwfaus8j293di192sjaei21nmdyr8qwdar9fxems"

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update({'DATABASE': os.path.join(app.root_path, 'homework.db')})


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with open('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()





@app.route('/index')
@app.route('/')
def index():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template("index.html", title='Главная',
                           menu=db.get_menu(),
                           posts=db.get_posts())


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    db_con = connect_db()
    db = DataBase(db_con)
    if request.method == 'POST':
        if len(request.form['title']) > 4 and len(request.form['text']) > 20:
            res = db.add_post(request.form['title'], request.form['text'], request.form['url'])
            if res:
                flash('Статья добавлена успешно', category='success')
            else:
                flash('Ошибка добавления статьи', category='error')
        else:
            flash('Ошибка добавления статьи', category='error')

    return render_template('add_post.html', title='Добавление статьи', menu=db.get_menu())


@app.route('/post/<post_id>')
def show_post(post_id):
    db_con = connect_db()
    db = DataBase(db_con)

    title, post = db.get_post(post_id)
    if not title:
        abort(404)
    return render_template('post.html', title=title, post=post, menu=db.get_menu())


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    db_con = connect_db()
    db = DataBase(db_con)
    context = {}
    if request.method == 'POST':
        if len(request.form['username']) > 1:
            flash('Сообщение отправлено успешно!', category='success')
        else:
            flash('Ошибка отправки!', category='error')
        context = {
            'username': request.form['username'],
            'email': request.form['email'],
            'message': request.form['message'],
        }

    return render_template('contacts.html', **context, title='Обратная связь', menu=db.get_menu())


@app.route('/profile/<string:username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'Пользователь {username}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'admin' \
            and request.form['password'] == 'admin':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Авторизация', menu=db.get_menu())

@app.route('/about')
def about():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('about.html', posts=db.get_about(), menu=db.get_menu())

@app.errorhandler(404)
def page_not_found(error):
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('page404.html', title='Страница не найдена', menu=db.get_menu()), 404


if __name__ == '__main__':
    create_db()
    app.run()
