def znak_out(znak="*", count=50):
    print(znak * count)


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

    def __init__(self):
        self.__model_name = input("Введите название модели: ")
        self.__year_of_issue = input("Введите год выпуска: ")
        self.__manufacturer = input("Введите завод изготовитель: ")
        self.__engin_capacity = input("Введите объем двигателя: ")
        self.__color_car = input("Введите цвет машины: ")
        self.__price_car = input("Введите цену машины: ")

    @property
    def model_name(self):
        return f"Модель: {self.__model_name}"

    @property
    def year_of_issue(self):
        return f"Год изготовления: {self.__year_of_issue}"

    @property
    def manufacturer(self):
        return f"Завод изготовитель: {self.__manufacturer}"

    @property
    def engin_capacity(self):
        return f"Объем двигателя: {self.__engin_capacity}"

    @engin_capacity.setter
    def engin_capacity(self, value):
        self.__engin_capacity = value

    @property
    def color_car(self):
        return f"Цвет кузова: {self.__color_car}"

    @color_car.setter
    def color_car(self, value):
        self.__color_car = value

    @property
    def price_car(self):
        return f"Цена автомобиля: {self.__price_car}"

    @price_car.setter
    def price_car(self, value):
        self.__price_car = value

    def get_info(self):
        return f"Данне модели:\n" \
               f"\t{self.model_name}\n" \
               f"\t{self.year_of_issue}\n" \
               f"\t{self.manufacturer}\n" \
               f"\t{self.engin_capacity}\n" \
               f"\t{self.color_car}\n" \
               f"\t{self.price_car}" \

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

    def __init__(self):
        self.__name_book = input("Введите название книги: ")
        self.__year_of_publishing = input("Введите год выпуска: ")
        self.__publisher = input("Введите издателя: ")
        self.__genre = input("Введите жанр: ")
        self.__author = input("Введите автора: ")

    @property
    def name_book(self):
        return f"Название книги: {self.__name_book}"

    @property
    def year_of_publishing(self):
        return f"Год последнего издания: {self.__year_of_publishing}"

    @year_of_publishing.setter
    def year_of_publishing(self, value):
        self.__year_of_publishing = value

    @property
    def publisher(self):
        return f"Издатель: {self.__publisher}"

    @publisher.setter
    def publisher(self, value):
        self.__publisher = value

    @property
    def genre(self):
        return f"Жанр: {self.__genre}"

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def author(self):
        return f"Автор: {self.__author}"

    def get_info(self):
        return f"Данные книги:\n" \
               f"\t{self.name_book}\n" \
               f"\t{self.year_of_publishing}\n" \
               f"\t{self.publisher}\n" \
               f"\t{self.genre}\n" \
               f"\t{self.author}"


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

    def __init__(self):
        self.__name_stadium = input("Введите название стадиона: ")
        self.__opening_date = input("Введите дату открытия: ")
        self.__country = input("Введите страну: ")
        self.__city = input("Введите город: ")
        self.__capacity = input("Введите вместимость: ")

    @property
    def name_stadium(self):
        return f"Название стадиона: {self.__name_stadium}"

    @name_stadium.setter
    def name_stadium(self, value):
        self.__name_stadium = value

    @property
    def opening_date(self):
        return f"Дата открытия: {self.__opening_date}"

    @opening_date.setter
    def opening_date(self, value):
        self.__opening_date = value

    @property
    def country(self):
        return f"Страна: {self.__country}"

    @country.setter
    def country(self, value):
        self.__country = value

    @property
    def city(self):
        return f"Город: {self.__city}"

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def capacity(self):
        return f"Вместимость стадиона: {self.__capacity}"

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    def get_info(self):
        return f"Данные стадиона:\n" \
               f"\t{self.name_stadium}\n" \
               f"\t{self.opening_date}\n" \
               f"\t{self.country}\n" \
               f"\t{self.city}\n" \
               f"\t{self.capacity}"


if __name__ == '__main__':
    print("Задание 1")
    my_car = Car()
    print(my_car.get_info())
    print(my_car.color_car)
    my_car.color_car = 'yellow'
    print(my_car.color_car)
    znak_out()
    print("Задание 2")
    my_book = Book()
    print(my_book.get_info())
    print(my_book.publisher)
    my_book.publisher = 'АСТ'
    print(my_book.publisher)
    znak_out()
    print("Задание 3")
    my_stadium = Stadium()
    print(my_stadium.get_info())
    print(my_stadium.capacity)
    my_stadium.capacity = 90000
    print(my_stadium.capacity)
    znak_out()
