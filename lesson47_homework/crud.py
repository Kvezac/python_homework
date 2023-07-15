from sqlalchemy import func

from models.models import Sales, Salesmen, Customers, Base

from models.database import Session, DATABASE_NAME

session = Session()


def all_items(name_table):
    return session.query(name_table)


def sales_by_salesman(id: int):
    result = session.query(Sales.date,
                           Sales.amount,
                           Customers.name,
                           Salesmen.name) \
        .join(Salesmen, Sales.salesman_id == Salesmen.id) \
        .join(Customers, Sales.customer_id == Customers.id) \
        .filter(Salesmen.id == id) \
        .all()
    return result


def max_value():
    result = session.query(Sales.id, func.max(Sales.amount)).all()
    return result


def min_value():
    result = session.query(Sales.id, func.min(Sales.amount)).all()
    return result


def max_sale_by_salesman(id: int):
    result = session.query(Sales.amount, func.max(Sales.amount)) \
        .join(Salesmen, Sales.salesman_id == Salesmen.id).filter(Salesmen.id == id).first()[0]
    return result


def min_sale_by_salesman(id: int):
    result = session.query(Sales.amount, func.min(Sales.amount)) \
        .join(Salesmen, Sales.salesman_id == Salesmen.id).filter(Salesmen.id == id).first()[0]
    return result


def max_sale_by_customers(id: int):
    result = session.query(Sales.amount, func.max(Sales.amount)) \
        .join(Customers, Sales.salesman_id == Customers.id).filter(Customers.id == id).first()[0]
    return result


def min_sale_by_customers(id: int):
    result = session.query(Sales.amount, func.min(Sales.amount)) \
        .join(Customers, Sales.salesman_id == Customers.id).filter(Customers.id == id).first()[0]
    return result


def max_sale_by_all_salesmen():
    pass


def min_sale_by_all_salesmen():
    pass


def max_sale_by_all_customers():
    pass


def min_sale_by_all_customers():
    pass


def avg_sale_by_salesman():
    pass


if __name__ == '__main__':
    print(max_sale_by_salesman(1))
