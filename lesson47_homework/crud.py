from models import Sales, Salesmen, Customers, Base, NAME_DATABASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f'sqlite:///{NAME_DATABASE}.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def all_items(name_table):
    return session.query(name_table).all()


def sales_by_salesman(id: int):
    # result = session.query(Sales.date, Sales.amount, Customers.name, Salesmen.name) \
    #     .join(Salesmen, Sales.salesman_id == Salesmen.id) \
    #     .join(Customers, Sales.customer_id == Customers.id) \
    #     .filter(Salesmen.id == id) \
    #     .all()
    # result = session.query(Sales.date, Sales.amount, Customers.name, Salesmen.name).filter(Salesmen.id == id).join(Salesmen, Sales.id == Salesmen.id).join(Customers, Sales.id == Customers.id).all()
    # result = session.query(Sales.date, Sales.amount, Customers.name, Salesmen.name
    #                        ).outerjoin(Salesmen, Sales.salesman_id == Salesmen.id).outerjoin(Customers, Sales.customer_id == Customers.id).filter(Salesmen.id == id).all()
    # result = session.query(Sales).join(Salesmen, Sales.salesman_id == Salesmen.id).filter(Salesmen.id == id)
    result = session.query(Sales.salesman_id).filter(Sales.salesman_id == id)
    # result = result.add_columns(Salesmen.id)
    return result


if __name__ == '__main__':
    # print(*all_items(Sales), sep='\n')
    # print(*all_items(Salesmen), sep='\n')
    query = sales_by_salesman(1)
    print(query)
    # # print(query)
    for row in query:
        print(row)
        # date, amount, customer_name, salesman_name = row
        # print(f"Date: {date.strftime('%Y-%m-%d')}, Amount: {amount}, Buyer: {customer_name}, Salesman: {salesman_name}")


# def sales_by_salesman():
#     session = Session()
#     salesman_id = request.args.get('salesman_id')
#     if salesman_id:
#         sales = session.query(Sales).filter_by(salesman_id=salesman_id).all()
#     else:
#         sales = session.query(Sales).all()
#     salesmen = session.query(Salesmen).all()
#     session.close()
#     return render_template('sales_by_salesman.html', sales=sales, salesmen=salesmen)
#
#
#
# def max_sale():
#     session = Session()
#     max_sale = session.query(Sales).order_by(Sales.amount.desc()).first()
#     session.close()
#     return render_template('max_sale.html', max_sale=max_sale)
#
#
#
# def min_sale():
#     session = Session()
#     min_sale = session.query(Sales).order_by(Sales.amount).first()
#     session.close()
#     return render_template('min_sale.html', min_sale=min_sale)
#
#
#
# def max_sale_by_salesman():
#     session = Session()
#     salesman_id = request.args.get('salesman_id')
#     if salesman_id:
#         max_sale = session.query(Sales).filter_by(salesman_id=salesman_id).order_by(Sales.amount.desc()).first()
#     else:
#         max_sale = session.query(Sales).order_by(Sales.amount.desc()).first()
#     salesmen = session.query(Salesmen).all()
#     session.close()
#     return render_template('max_sale_by_salesman.html', max_sale=max_sale, salesmen=salesmen)
#
#
#
# def min_sale_by_salesman():
#     session = Session()
#     salesman_id = request.args.get('salesman_id')
#     if salesman_id:
#         min_sale = session.query(Sales).filter_by(salesman_id=salesman_id).order_by(Sales.amount).first()
#     else:
#         min_sale = session.query(Sales).order_by(Sales.amount).first()
#     salesmen = session.query(Salesmen).all()
#     session.close()
#     return render_template('min_sale_by_salesman.html', min_sale=min_sale, salesmen=salesmen)
#
#
#
# def max_sale_by_customer():
#     session = Session()
#     customer_id = request.args.get('customer_id')
#     if customer_id:
#         max_sale = session.query(Sales).filter_by(customer_id=customer_id).order_by(Sales.amount.desc()).first()
#     else:
#         max_sale = session.query(Sales).order_by(Sales.amount.desc()).first()
#     customers = session.query(Customers).all()
#     session.close()
#     return render_template('max_sale_by_customer.html', max_sale=max_sale, customers=customers)
#
#
#
# def min_sale_by_customer():
#     session = Session()
#     customer_id = request.args.get('customer_id')
#     if customer_id:
#         min_sale = session.query(Sales).filter_by(customer_id=customer_id).order_by(Sales.amount).first()
#     else:
#         min_sale = session.query(Sales).order_by(Sales.amount).first()
#     customers = session.query(Customers).all()
#     session.close()
#     return render_template('min_sale_by_customer.html', min_sale=min_sale, customers=customers)
#
#
#
# def max_sale_by_all_salesmen():
#     session = Session()
#     max_sale = session.query(Sales).order_by(Sales.amount.desc()).first()
#     salesman = session.query(Salesmen).filterОпечатка, продолжение:
#
#     (Salesmen.id == max_sale.salesman_id).first()
#     session.close()
#     return render_template('max_sale_by_all_salesmen.html', max_sale=max_sale, salesman=salesman)
#
#
#
# def min_sale_by_all_salesmen():
#     session = Session()
#     min_sale = session.query(Sales).order_by(Sales.amount).first()
#     salesman = session.query(Salesmen).filter(
#         Salesmen.id == min_sale.salesman_id).first()
#     session.close()
#     return render_template('min_sale_by_all_salesmen.html', min_sale=min_sale, salesman=salesman)
#
#
# @app.route('/max_sale_by_all_customers')
# def max_sale_by_all_customers():
#     session = Session()
#     max_sale = session.query(Sales).order_by(Sales.amount.desc()).first()
#     customer = session.query(Customers).filter(
#         Customers.id == max_sale.customer_id).first()
#     session.close()
#     return render_template('max_sale_by_all_customers.html', max_sale=max_sale, customer=customer)
#
#
# @app.route('/avg_sale_by_customer')
# def avg_sale_by_customer():
#     session = Session()
#     customer_id = request.args.get('customer_id')
#     if customer_id:
#         avg_sale = session.query(func.avg(Sales.amount)).filter_by(customer_id=customer_id).scalar()
#         customer = session.query(Customers).filter_by(id=customer_id).first()
#     else:
#         avg_sale = None
#         customer = None
#     customers = session.query(Customers).all()
#     session.close()
#     return render_template('avg_sale_by_customer.html', avg_sale=avg_sale, customer=customer, customers=customers)
#
#
# @app.route('/avg_sale_by_salesman')
# def avg_sale_by_salesman():
#     session = Session()
#     salesman_id = request.args.get('salesman_id')
#     if salesman_id:
#         avg_sale = session.query(func.avg(Sales.amount)).filter_by(salesman_id=salesman_id).scalar()
#         salesman = session.query(Salesmen).filter_by(id=salesman_id).first()
#     else:
#         avg_sale = None
#         salesman = None
#     salesmen = session.query(Salesmen).all()
#     session.close()
#     return render_template('avg_sale_by_salesman.html', avg_sale=avg_sale, salesman=salesman, salesmen=salesmen)
