import math


class Fraction:
    """ Создать класс 'Дробь'. Необходимо хранить в полях класса:
        - числитель
        - знаменатель
    Реализуйте методы класса для ввода данных, вывода данных,
    доступ к полям через методы класса.
    Также создайте методы класса для выполнения арифметических операций:
        - сложение
        - вычитание
        - умножение
        - деление
    Добавить статических методов который при вызове возвращает количество созданных
    объектов
    """
    count = 0

    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
        self.__class__.count += 1

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, value):
        if value > 0:
            self.__top = value
        else:
            raise "Значение не может быть равным 0"

    @property
    def bottom(self):
        return self.__bottom

    @bottom.setter
    def bottom(self, value):
        if value > 0:
            self.__bottom = value
        else:
            raise "Значение не может быть равным 0"

    def adding(self, other):
        new_top = self.top * other.bottom + self.bottom * other.top
        new_b = self.bottom * other.bottom
        our_gcd = math.gcd(new_top, new_b)
        return f'{new_top // our_gcd} / {new_b // our_gcd}'

    def subtraction(self, other):
        new_top = self.top * other.bottom - self.bottom * other.top
        new_b = self.bottom * other.bottom
        our_gcd = math.gcd(new_top, new_b)
        return f'{new_top // our_gcd} / {new_b // our_gcd}'

    def multiplication(self, other):
        new_top = self.top * other.top
        new_b = self.bottom * other.bottom
        our_gcd = math.gcd(new_top, new_b)
        return f'{new_top // our_gcd} / {new_b // our_gcd}'

    def division(self, other):
        new_top = self.top * other.bottom
        new_b = self.bottom * other.top
        our_gcd = math.gcd(new_top, new_b)
        return f'{new_top // our_gcd} / {new_b // our_gcd}'

    @classmethod
    def count_fraction(cls):
        return f"Количество инициализированных объектов: {cls.count}"

    def get_info(self):
        return f"{self.top} / {self.bottom}"


class Convector:
    """ Создайте класс для конвертирования температуры из
        Цельсия Фаренгейт и наоборот. У класса должно быть
        два статических метода: для перевода из Цельсия Фаренгейт
        и для перевода из Фаренгейта Цельсий. Также
        класс должен считать количество подсчетов температуры и
        возвращать это значение с помощью статического метода.

    """
    count = 0

    @staticmethod
    def celsius(value):
        Convector.count += 1
        return f'Перевод из фаренгейта в цельсия: {round((value - 32) / 1.8, 2)}'

    @staticmethod
    def fahrenheit(value):
        Convector.count += 1
        return f'Перевод из цельсия в фаренгейт: {round((value * 1.8) + 32, 2)}'

    @classmethod
    def amount(cls):
        return f'Количество операций: {cls.count}'


class System:
    """ Создайте класс для перевода из метрической системы
        в английскую и наоборот. Функциональность необходимо
        реализовать в виде статических методов. Обязательно
        реализуйте перевод мер длины.
    """

    @staticmethod
    def inch(value):
        return f"{value} сантиметров равно {value / 2.5} дюймов"

    @staticmethod
    def centimetres_inch(value):
        return f"{value} дюймов равно {value * 2.5} сантиметров"

    @staticmethod
    def foot(value):
        return f"{value} сантиметров равно {round(value / 30.5, 3)} фут"

    @staticmethod
    def centimetres_foot(value):
        return f"{value} фут равно {value * 30.5} сантиметров"

    @staticmethod
    def mile(value):
        return f"{value} км равно {round(value / 1.6, 3)} миль"

    @staticmethod
    def km(value):
        return f"{value} миль равно {value * 1.6} километров"

    @staticmethod
    def ounce(value):
        return f"{value} грамм равно {round(value / 28.4, 3)} унций"

    @staticmethod
    def grams_ounce(value):
        return f"{value} унций равно {value} грамм"

    @staticmethod
    def poud(value):
        return f"{value} гамм равно {round(value / 453.6, 3)} фунт(ов)"

    @staticmethod
    def grams_pounds(value):
        return f"{value} фунтов равно {value * 483.6} грамм"


if __name__ == "__main__":
    while (user_inp := input("Выбираем задание:\n"
                             "\t1 Дробь\n"
                             "\t2 Конвектор температур\n"
                             "\t3 Перевод из метрической в английскую\n"
                             "\t0 Выход\n: ")) != '0':
        match user_inp:
            case '1':
                my_1 = Fraction(1, 5)
                print(my_1.get_info())
                my_2 = Fraction(1, 2)
                print(my_2.get_info())
                print(Fraction.count_fraction())
                print(my_1.adding(my_2))
                print(my_1.subtraction(my_2))
                my_3 = Fraction(5, 9)
                print(Fraction.count_fraction())
                print(my_3.get_info())
                print(my_1.multiplication(my_3))
                print(my_2.division(my_3))
            case '2':
                temp = Convector()
                print(temp.celsius(102))
                print(temp.fahrenheit(-11))
                print(temp.amount())
            case '3':
                metr = System()
                print(metr.poud(100))
                print(metr.inch(10003))
                print(metr.centimetres_inch(10))
                print(metr.poud(100))
                print(metr.centimetres_foot(50))
                print(metr.mile(1000))
                print(metr.km(50))

            case _:
                print("Сейчас этим займемся.")
    print("Программа завершена.\nДо скорой встречи.")
