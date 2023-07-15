import os

from crud import all_items, \
    sales_by_salesman, \
    max_value, \
    min_value, \
    max_sale_by_salesman, min_sale_by_salesman, max_sale_by_customers, min_sale_by_customers
from models.database import DATABASE_NAME
import create_database as db_creator

from lesson47_homework.models.models import Sales, Salesmen, Customers


def main():
    while (query := input('Choose a command to execute\n'
                          '1. Sample Requests\n: ')) != '0':
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
                                        '10. \n'
                                        '11. \n'
                                        '12. \n'
                                        '13. \n: ')) != '0':
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
                            pass
                        case '10':
                            pass
                        case '11':
                            pass
                        case '12':
                            pass
                        case '13':
                            pass

                        case _:
                            print('There is no command like this.')
                else:
                    print('Exit to main menu')

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
