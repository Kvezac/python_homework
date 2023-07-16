import os

from crud import all_items, \
    sales_by_salesman, \
    max_value, \
    min_value, \
    max_sale_by_salesman, \
    min_sale_by_salesman, \
    max_sale_by_customers, \
    min_sale_by_customers, \
    max_sale_by_all_salesmen, \
    min_sale_by_all_salesmen, \
    max_sale_by_all_customers, \
    avg_sale_by_customers, \
    avg_sale_by_salesman, \
    key_request, \
    update_sale, \
    update_customers, \
    update_salesman, \
    insert_table,\
    delete_entry
from models.database import DATABASE_NAME
import create_database as db_creator

from lesson47_homework.models.models import Sales, Salesmen, Customers


def main():
    while (query := input('Choose a command to execute\n'
                          '1. Sample Requests\n'
                          '2. Creat, Insert, Delete\n: ')) != '0':
        match query:
            case '1':
                while (request := input('Choose a command to execute\n'
                                        '1. Display all trades\n'
                                        '2. Show deals of a particular seller\n'
                                        '3. Displaying the maximum amount of the transaction\n'
                                        '4. Displaying the minimum amount of the transaction\n'
                                        '5. Displaying the maximum amount of the transaction for a particular seller\n'
                                        '6. Displaying the minimum transaction amount for a particular seller\n'
                                        '7. Displaying the maximum transaction amount for a particular buyer \n'
                                        '8. Displaying the minimum transaction amount for a specific buyer\n'
                                        '9. Displaying the seller who has the maximum amount of sales for all '
                                        'transactions \n'
                                        '10. Displaying the seller who has the minimum amount of sales for all '
                                        'transactions\n'
                                        '11. Displaying the buyer who has the maximum amount of purchases across all '
                                        'transactions\n'
                                        '12. Displaying the average purchase amount for a particular customer\n'
                                        '13. Displaying the average purchase amount for a particular seller\n: ')) != '0':
                    match request:
                        case '1':
                            db_query = all_items(Sales)
                            [print(i) for i in db_query]
                        case '2':
                            all_seller = all_items(Salesmen)
                            [print(i.id, i.name) for i in all_seller]
                            id_inp = input('Select id seller\n: ')
                            db_query = sales_by_salesman(int(id_inp))
                            for row in db_query:
                                date, amount, customer_name, salesman_name = row
                                print(
                                    f"Date: {date.strftime('%d.%m.%Y')}, Amount: {amount}, Buyer: {customer_name}, Salesman: {salesman_name}")
                        case '3':
                            db_query = max_value()[0]
                            print(f'id: {db_query[0]} max amount: {db_query[1]}')
                        case '4':
                            db_query = min_value()[0]
                            print(f'id {db_query[0]} min amount: {db_query[1]}')
                        case '5':
                            all_seller = all_items(Salesmen)
                            [print(i.id, i.name) for i in all_seller]
                            id_inp = input('Select id seller\n: ')
                            query = max_sale_by_salesman(id_inp)
                            print(query)
                        case '6':
                            all_seller = all_items(Salesmen)
                            [print(i.id, i.name) for i in all_seller]
                            id_inp = input('Select id seller\n: ')
                            query = min_sale_by_salesman(id_inp)
                            print(query)
                        case '7':
                            all_bayer = all_items(Customers)
                            [print(i.id, i.name) for i in all_bayer]
                            id_inp = input('Select id customer\n: ')
                            query = max_sale_by_customers(id_inp)
                            print(query)
                        case '8':
                            all_bayer = all_items(Customers)
                            [print(i.id, i.name) for i in all_bayer]
                            id_inp = input('Select id customer\n: ')
                            query = min_sale_by_customers(id_inp)
                            print(query)
                        case '9':
                            print(max_sale_by_all_salesmen())
                        case '10':
                            print(min_sale_by_all_salesmen())
                        case '11':
                            print(max_sale_by_all_customers())
                        case '12':
                            print(avg_sale_by_customers())
                        case '13':
                            print(avg_sale_by_salesman())

                        case _:
                            print('There is no command like this.')
                else:
                    print('Exit to main menu')
            case '2':
                while (request := input('Choose a command to execute\n'
                                        '1. Update an entry in a table Sales\n'
                                        '2. Update an entry in a table Customers\n'
                                        '3. Update an entry in a table Salesmen\n'
                                        '4. Add a new entry to the table Sales\n'
                                        '4. Add a new entry to the table Customers\n'
                                        '6. Add a new entry to the table Salesmen\n'
                                        '7. Delete record from table Sales\n'
                                        '8. Delete record from table Customers\n'
                                        '9. Delete record from table Salesmen\n: ')) != '0':
                    match request:
                        case '1':
                            sale_query = all_items(Sales)
                            [print(i) for i in sale_query]
                            sale_id = int(input("Enter the ID of the sale to be updated: "))
                            sale = key_request(Sales, sale_id)
                            if sale:
                                salesmen_query = all_items(Salesmen)
                                [print(i) for i in salesmen_query]
                                salesman_id = int(input("Enter a new seller ID: "))
                                customer_query = all_items(Customers)
                                [print(i) for i in customer_query]
                                customer_id = int(input("Enter a new buyer ID: "))
                                amount = int(input("Enter new sales amount: "))
                                update_sale(sale_id, salesman_id, customer_id, amount)

                            else:
                                print("Sale with this ID was not found")
                        case '2':
                            customer_query = all_items(Customers)
                            [print(i) for i in customer_query]
                            customers_id = int(input("Enter the ID of the customers to be updated: "))
                            customer = key_request(Customers, customers_id)
                            if customer:
                                name = input('Enter new name buyer')
                                update_customers(customers_id, name)
                            else:
                                print("Sale with this ID was not found")

                        case '3':
                            salesmen_query = all_items(Salesmen)
                            [print(i) for i in salesmen_query]
                            salesmen_id = int(input("Enter the ID of the salesmen to be updated: "))
                            salesmen = key_request(Salesmen, salesmen_id)
                            if salesmen:
                                name = int(input("Enter a new salesmen ID: "))
                                update_salesman(salesmen_id, name)
                            else:
                                print("Sale with this ID was not found")
                        case '4':
                            date = input("Enter date in YYYY-MM-DD format: ")
                            salesman_id = input("Enter Seller ID: ")
                            customer_id = input("Enter Buyer ID: ")
                            amount = input("Enter the amount of the sale: ")
                            sale = Sales(date=date, salesman_id=salesman_id,
                                         customer_id=customer_id, amount=amount)
                            insert_table(sale)
                        case '5':
                            name = input("Enter buyer's name: ")
                            buyer = Customers(name=name)
                            insert_table(buyer)
                        case '6':
                            name = input("Enter seller name: ")
                            salesmen = Salesmen(name=name)
                            insert_table(salesmen)
                        case '7':
                            sale_id = int(input("Enter Sales ID: "))
                            sale = key_request(Sales, sale_id)
                            if sale:
                                delete_entry(sale)
                            else:
                                print("Sale with this ID was not found")

                        case '8':
                            buyer_id = int(input("Enter the ID of the customers: "))
                            buyer = key_request(Customers, buyer_id)
                            if buyer:
                                delete_entry(buyer_id)
                            else:
                                print("Sale with this ID was not found")
                        case '9':
                            seller_id = int(input("Enter the ID of the seller: "))
                            buyer = key_request(Salesmen, seller_id)
                            if buyer:
                                delete_entry(seller_id)
                            else:
                                print("Sale with this ID was not found")
                        case _:
                            print('There is no command like this.')

            case _:
                print('There is no command like this.')
    else:
        print('Program finish')


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
        print('Create:', DATABASE_NAME)
    else:
        print(DATABASE_NAME, 'exists')

    main()
