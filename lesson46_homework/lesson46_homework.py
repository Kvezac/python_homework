import sqlite3 as sq
import csv

with sq.connect('database.db') as conn:
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    product TEXT,
                    price REAL,
                    FOREIGN KEY (user_id) REFERENCES users(id))''')

    # Наполнение таблиц данными
    with open('users.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # пропустить заголовок
        for row in reader:
            name, age = str(*row).split(',')
            cur.execute("INSERT INTO users VALUES (Null, ?, ?)", (name, age))

    product_list = [(1, 'Телефон', 500),
                    (3, 'Ноутбук', 1000),
                    (3, 'Наушники', 200)]

    cur.executemany('''INSERT INTO orders VALUES(Null, ?, ?, ?)''', product_list)

    # Получить список всех пользователей и их возраст:
    cur.execute("SELECT name, age FROM users")
    print(cur.fetchall())
    # Получить список всех заказов, упорядоченных по возрастанию цены
    cur.execute("SELECT * FROM orders ORDER BY price")
    print(cur.fetchall())
    # Получить список всех заказов, сделанных для конкретного пользователя
    cur.execute("SELECT * FROM orders WHERE user_id=1")
    print(cur.fetchall())
    # Получить суммарную стоимость всех заказов для каждого пользователя
    cur.execute('''SELECT users.name, SUM(orders.price)
                FROM users JOIN orders ON users.id = orders.user_id
                GROUP BY users.id''')
    print(cur.fetchall())
    # Получить список всех заказов, сделанных на определенный продукт
    cur.execute("SELECT * FROM orders WHERE product='Наушники'")
    print(cur.fetchall())
    # Получить список всех пользователей, у которых нет заказов
    cur.execute('''SELECT users.name
                   FROM users LEFT JOIN orders ON users.id = orders.user_id
                   WHERE orders.id IS NULL''')
    print(cur.fetchall())
