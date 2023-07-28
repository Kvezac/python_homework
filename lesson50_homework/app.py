import sqlite3
import os

from flask import Flask, render_template

from DataBase import DataBase

DATABASE = '/tmp/homework.db'
DEBUG = True
SECRET_KEY = "124ugftyedar9fxekPOPms"

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


@app.route('/')
def index():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template("index.html", title='Главная',
                           menu=db.get_menu())


@app.route('/about')
def about():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('about.html', title='О сайте', menu=db.get_menu())


@app.route('/contacts')
def contacts():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('contacts.html', title='Обратная связь', menu=db.get_menu)


if __name__ == '__main__':
    create_db()
    app.run()
