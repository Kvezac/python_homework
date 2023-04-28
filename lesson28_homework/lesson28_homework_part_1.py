import json
import pickle


class Car:
    """ Реализуйте класс «Автомобиль».
        Необходимо хранить в полях класса:
            - название модели
            - год выпуска
            - производителя
            - объем двигателя
            - цвет машины
            - цену.
        Реализуйте методы класса:
            - для ввода данных
            - вывода данных
        *реализуйте доступ к отдельным полям через методы класса. SET не использовать
    """

    def __init__(self, model_name: str = None,
                 year_of_issue: int = None,
                 manufacturer: str = None,
                 engin_capacity: int | float = None,
                 color_car: str = None,
                 price_car: int | float = None) -> None:
        self.model_name = model_name if model_name else input("Введите название модели: ")
        self.year_of_issue = year_of_issue if year_of_issue else input("Введите год выпуска: ")
        self.manufacturer = manufacturer if manufacturer else input("Введите завод изготовитель: ")
        self.engin_capacity = engin_capacity if engin_capacity else input("Введите объем двигателя: ")
        self.color_car = color_car if color_car else input("Введите цвет машины: ")
        self.price_car = price_car if price_car else input("Введите цену машины: ")

    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value

    @property
    def year_of_issue(self):
        return self._year_of_issue

    @year_of_issue.setter
    def year_of_issue(self, value):
        self._year_of_issue = value

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value

    @property
    def engin_capacity(self):
        return self._engin_capacity

    @engin_capacity.setter
    def engin_capacity(self, value):
        self._engin_capacity = value

    @property
    def color_car(self):
        return self._color_car

    @color_car.setter
    def color_car(self, value):
        self._color_car = value

    @property
    def price_car(self):
        return self._price_car

    @price_car.setter
    def price_car(self, value):
        self._price_car = value

    def __repr__(self):
        return {self.__class__.__name__: self.__dict__}

    def __str__(self):
        return f"Информация о модели:\n" \
               f"Модель: {self.model_name}\n" \
               f"Год изготовления: {self.year_of_issue}\n" \
               f"Завод изготовитель: {self.manufacturer}\n" \
               f"Объем двигателя: {self.engin_capacity}\n" \
               f"Цвет кузова: {self.color_car}\n" \
               f"Цена автомобиля: {self.price_car}"

    def save_car_json(self):
        with open('car.txt', 'a', encoding='utf-8') as f:
            json.dump(self.__repr__(), f, ensure_ascii=False)
            f.write('\n')
        print('Save json complete')

    @classmethod
    def load_car_json(cls):
        car_list = []
        with open('car.txt', 'r', encoding='utf-8') as f:
            data = (json.loads(i.strip()) for i in f)
            for value in data:
                car_list.append(Car(value['Car']['_model_name'],
                                    value['Car']['_year_of_issue'],
                                    value['Car']['_manufacturer'],
                                    value['Car']['_engin_capacity'],
                                    value['Car']['_color_car'],
                                    value['Car']['_price_car']))
        return car_list

    def save_car_pickle(self):
        with open('car.bin', 'ab') as f:
            pickle.dump((self.__class__, self.__dict__), f)
        print('Save pickle complete')

    @classmethod
    def load_car_pickle(cls):
        data = []
        # car_list = []
        with open("car.bin", "rb") as f:
            while True:
                try:
                    log = pickle.load(f)
                    data.append(log[0](*log[1].values()))
                except EOFError:
                    break
        return data


class Book:
    """ Реализуйте класс «Книга».
        Необходимо хранить в полях класса:
            - название книги
            - год выпуска
            - издателя
            - жанр
            - автора
            - цену.
        Реализуйте методы класса:
            - для ввода
            - данных
            - вывода данных
        *реализуйте доступ к отдельным полям через методы класса.
    """

    def __init__(self, name_book: str = None,
                 year_of_publishing: int = None,
                 publisher: str = None,
                 genre: str = None,
                 author: str = None):
        self.name_book = name_book if name_book else input("Введите название книги: ")
        self.year_of_publishing = year_of_publishing if year_of_publishing else input("Введите год выпуска: ")
        self.publisher = publisher if publisher else input("Введите издателя: ")
        self.genre = genre if genre else input("Введите жанр: ")
        self.author = author if author else input("Введите автора: ")

    @property
    def name_book(self):
        return self._name_book

    @name_book.setter
    def name_book(self, value):
        self._name_book = value

    @property
    def year_of_publishing(self):
        return self._year_of_publishing

    @year_of_publishing.setter
    def year_of_publishing(self, value):
        self._year_of_publishing = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    def __repr__(self):
        return {self.__class__.__name__: self.__dict__}

    def __str__(self):
        return f"Данные книги:\n" \
               f"Название книги: {self._name_book}\n" \
               f"\tГод последнего издания: {self._year_of_publishing}\n" \
               f"\tИздатель: {self._publisher}\n" \
               f"\tЖанр: {self._genre}\n" \
               f"\tАвтор: {self._author}"

    def save_book_json(self):
        with open('book.txt', 'a', encoding='utf-8') as f:
            json.dump(self.__repr__(), f, ensure_ascii=False)
            f.write('\n')
        print('Save json complete')

    @classmethod
    def load_book_json(cls):
        book_list = []
        with open('book.txt', 'r', encoding='utf-8') as f:
            data = (json.loads(i.strip()) for i in f)
            for value in data:
                book_list.append(Book(value['Book']['_name_book'],
                                      value['Book']['_year_of_publishing'],
                                      value['Book']['_publisher'],
                                      value['Book']['_genre'],
                                      value['Book']['_author']))
        return book_list

    def save_book_pickle(self):
        with open('book.bin', 'ab') as f:
            pickle.dump((self.__class__, self.__dict__), f)
        print('Save pickle complete')

    @classmethod
    def load_book_pickle(cls):
        data = []
        # car_list = []
        with open("book.bin", "rb") as f:
            while True:
                try:
                    log = pickle.load(f)
                    data.append(log[0](*log[1].values()))
                except EOFError:
                    break
        return data


class Stadium:
    """Реализуйте класс «Стадион».
        Необходимо хранить в полях класса:
            - название стадиона
            - дату открытия
            - страну
            - город
            - вместимость.
        Реализуйте методы класса:
            - для ввода данных
            - вывода данных
        *реализуйте доступ к отдельным полям через методы класса.
    """

    def __init__(self,
                 name_stadium: str = None,
                 opening_date: int = None,
                 country: str = None,
                 city: str = None,
                 capacity: int | float = None):
        self.name_stadium = name_stadium if name_stadium else input("Введите название стадиона: ")
        self.opening_date = opening_date if opening_date else input("Введите дату открытия: ")
        self.country = country if country else input("Введите страну: ")
        self.city = city if city else input("Введите город: ")
        self.capacity = capacity if capacity else input("Введите вместимость: ")

    @property
    def name_stadium(self):
        return self._name_stadium

    @name_stadium.setter
    def name_stadium(self, value):
        self._name_stadium = value

    @property
    def opening_date(self):
        return self._opening_date

    @opening_date.setter
    def opening_date(self, value):
        self._opening_date = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        try:
            if int(value):
                self._capacity = value
        except ValueError:
            raise f"Должно быть число."

    def __repr__(self):
        return {self.__class__.__name__: self.__dict__}

    def __str__(self):
        return f"Данные стадиона:\n" \
               f"\tНазвание стадиона: {self._name_stadium}\n" \
               f"\tДата открытия: {self._opening_date}\n" \
               f"\tСтрана: {self._country}\n" \
               f"\tГород: {self._city}\n" \
               f"\tВместимость стадиона: {self._capacity}"

    def save_stadium_json(self):
        with open('stadium.txt', 'a', encoding='utf-8') as f:
            json.dump(self.__repr__(), f, ensure_ascii=False)
            f.write('\n')
        print('Save json complete')

    @classmethod
    def load_stadium_json(cls):
        stadium_list = []
        with open('stadium.txt', 'r', encoding='utf-8') as f:
            data = (json.loads(i.strip()) for i in f)
            for value in data:
                stadium_list.append(Stadium(value['Stadium']['_name_stadium'],
                                         value['Stadium']['_opening_date'],
                                         value['Stadium']['_country'],
                                         value['Stadium']['_city'],
                                         value['Stadium']['_capacity']))
        return stadium_list

    def save_stadium_pickle(self):
        with open('stadium.bin', 'ab') as f:
            pickle.dump((self.__class__, self.__dict__), f)
        print('Save pickle complete')

    @classmethod
    def load_stadium_pickle(cls):
        data = []
        with open("stadium.bin", "rb") as f:
            while True:
                try:
                    log = pickle.load(f)
                    data.append(log[0](*log[1].values()))
                except EOFError:
                    break
        return data


def demarcation_line(line="*", count=50):
    print(line * count)


def main():
    while (user_log := input("Choose a command to execute:\n"
                             "1 Class Car\n"
                             "2 class Book\n"
                             "3 class Stadium\n"
                             "0 Exit\n: ")) != 0:
        match user_log:

            case '1':
                my_car = Car()
                new_my_car = Car('Prado', 1985, 'Toyota', 3.5, 'Black', 35_0000)
                demarcation_line()
                my_car.save_car_json()
                demarcation_line()
                new_my_car.save_car_json()
                c = Car.load_car_json()
                for i in c:
                    demarcation_line()
                    print(i)
                new_my_car.save_car_pickle()
                demarcation_line()
                p = my_car.load_car_pickle()
                [print(i, end=demarcation_line()) for i in p]

            case '2':
                my_book = Book()
                next_new_book = Book("Learning Python", 2019, 'O`Reilly', 'Programming', 'Mark Lutz')
                my_book.save_book_json()
                next_new_book.save_book_pickle()
                b = Book.load_book_json()
                for i in b:
                    demarcation_line()
                    print(i)
                p = Book.load_book_pickle()
                for i in p:
                    demarcation_line()
                    print(i)

            case '3':
                my_stadium = Stadium()
                new_my_stadium = Stadium("Arena", 2018, "Russia", "St.Petersburg", 10000)
                my_stadium.save_stadium_json()
                new_my_stadium.save_stadium_pickle()
                s = Stadium.load_stadium_json()
                [print(i, end=demarcation_line()) for i in s]
                sp = Stadium.load_stadium_pickle()
                [print(i, end=demarcation_line()) for i in sp]

            case _:
                print('There is no command like this')
                demarcation_line('-')

    print('Program finish')


if __name__ == '__main__':
    main()
