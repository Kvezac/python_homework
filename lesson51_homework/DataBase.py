import sqlite3
from time import time


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def _get_objects(self, table):
        try:
            self.__cur.execute(f'SELECT * from {table}')
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения данных')
        return []

    def get_menu(self):
        return self._get_objects('menu')

    def get_posts(self):
        return self._get_objects('posts')

    def get_about(self):
        return self._get_objects('about')

    def add_post(self, title, text, url):
        try:
            self.__cur.execute('SELECT COUNT() as "count" FROM posts WHERE url = "{url}"')
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Статья с таким URL уже существует')
                return False

            tm = time()
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)',
                               (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления в базу данных', e)
            return False
        return True

    def get_post(self, post_id):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE url == "{post_id}"')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения статьи из базы данных', e)
        return None, None
