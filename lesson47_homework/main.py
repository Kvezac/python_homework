import os

from models.database import DATABASE_NAME
import lesson47_homework.create_database as db_creator

# from models.models import Sales, Salesmen, Customers

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
        print('Create:', DATABASE_NAME)
    else:
        print(DATABASE_NAME)