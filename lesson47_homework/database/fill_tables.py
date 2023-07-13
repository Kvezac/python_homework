from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Sales, Salesmen, Customers, Base

engine = create_engine('sqlite:///sales.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker('ru-RU')

# Заполнение таблицы Salesmen
for _ in range(20):
    name = fake.name()
    salesman = Salesmen(name=name)
    session.add(salesman)

# Заполнение таблицы Customers
for _ in range(5):
    name = fake.company()
    customer = Customers(name=name)
    session.add(customer)

# Заполнение таблицы Sales
for _ in range(50):
    salesman_id = fake.random_int(min=1, max=20)
    customer_id = fake.random_int(min=1, max=5)
    date = fake.date_between(start_date='-3y', end_date='today')
    print(date)
    amount = fake.random_int(min=10, max=10000)
    sale = Sales(date=date, salesman_id=salesman_id, customer_id=customer_id, amount=amount)
    session.add(sale)

session.commit()
print("Database created")
session.close()
