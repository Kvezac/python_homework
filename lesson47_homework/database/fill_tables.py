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
    product = fake.word()
    price = fake.random_int(min=10, max=1000)
    sale = Sales(salesman_id=salesman_id, customer_id=customer_id, product=product, price=price)
    session.add(sale)

session.commit()
print("Database created")
session.close()
