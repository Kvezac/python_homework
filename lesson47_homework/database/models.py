import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    date = Column(DATE, default=datetime.date.year)
    salesman_id = Column(Integer, ForeignKey('salesmen.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    # product = Column(String)
    amount = Column(Integer)


class Salesmen(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
