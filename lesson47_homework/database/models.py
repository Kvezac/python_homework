from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    salesman_id = Column(Integer, ForeignKey('salesmen.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    salesman = relationship("Salesmen", back_populates="sales")
    customer = relationship("Customers", back_populates="sales")


class Salesmen(Base):
    __tablename__ = 'salesmen'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    sales = relationship("Sales", back_populates="salesman")


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    sales = relationship("Sales", back_populates="customer")

