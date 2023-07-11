from sqlalchemy import create_engine
from models import *


def main():
    engine = create_engine('sqlite:///sales.db', echo=True)

    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
