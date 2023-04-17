import math


class Circle:
    """ Создайте класс Circle (окружность). Для данного
        класса реализуйте ряд перегруженных операторов:
    ■ Проверка на равенство радиусов двух окружностей (операция ==);
    ■ Сравнения длин двух окружностей (операции >, <, <=,>=);
    ■ Пропорциональное изменение размеров окружности,
       путем изменения ее радиуса (операции + - += -=).
    """

    def __init__(self, radius: int | float) -> None:
        Circle.check_number(radius)
        # if not isinstance(radius, (int, float)):
        #     raise TypeError("Число должно быть целым или вещественным")
        self.radius = radius

    @classmethod
    def check_number(cls, number: int | float) -> None:
        if not isinstance(number, (int, float)):
            raise TypeError("Число должно быть целым или вещественным")

    def perimetr(self) -> float:
        """ Расчет длины окружности"""
        return 2 * math.pi * self.radius

    def __eq__(self, other) -> bool:
        """ Проверка на равенство == окружностей"""
        return self.radius == other.radius

    def __lt__(self, other) -> bool:
        """ Проверка на меньше < длинам окружности"""
        return self.perimetr() < other.perimetr()

    def __le__(self, other):
        """" Проверка на <= по длинам окружности"""
        return self.perimetr() <= other.perimetr()

    def __add__(self, num: int | float):
        Circle.check_number(num)

        # if not isinstance(num, (int, float)):
        #     raise TypeError("Должно быть целое, вещественное число")
        self.radius = self.radius + num

    def __iadd__(self, num: int | float):
        Circle.check_number(num)

        # if not isinstance(num, (int, float)):
        #     raise TypeError("Должно быть целое, вещественное число")
        self.radius += num

    def __sub__(self, num: int | float):
        Circle.check_number(num)
        # if not isinstance(num, (int, float)):
        #     raise TypeError("Должно быть целое, вещественное число")
        self.radius = self.radius - num

    def __isub__(self, num: int | float):
        Circle.check_number(num)
        # if not isinstance(num, (int, float)):
        #     raise TypeError("Должно быть целое, вещественное число")
        self.radius -= num

    def __repr__(self):
        return f'{self.__class__}: {self.radius}'

    def __str__(self):
        return f'Окружность с радиусом: {self.radius}'


class Complex:
    """ Создайте класс Complex (комплексное число).
        Создайте перегруженные операторы для реализации
        арифметических операций для по работе с комплексными
        числами (операции +, -, *, /).
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.__class__}: a={self.a}, b={self.b}'

    def __str__(self):
        return f'({self.a}{self.b:+}i)'

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Complex(new_a, new_b)

    def __sub__(self, other):
        new_a = self.a - other.a
        new_b = self.b - other.b
        return Complex(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.a * other.b + self.b * other.a
        return Complex(new_a, new_b)

    def __truediv__(self, other):
        denom = other.a ** 2 + other.b ** 2
        new_a = (self.a * other.a + self.b * other.b) / denom
        new_b = (self.b * other.a - self.a * other.b) / denom
        return Complex(new_a, new_b)


class Airplane:
    """ Вам необходимо создать класс Airplane (самолет).
        С помощью перегрузки операторов реализовать:
        ■ Проверка на равенство типов самолетов (операция = =);
        ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
        ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >< <= >=).
    """

    def __init__(self, model_airplane: str, type_airplane: str, passenger_capacity: int, passengers_on_board: int = 0):
        self.model_airplane = model_airplane
        self.type_airplane = type_airplane
        self.passenger_capacity = passenger_capacity
        try:
            if passengers_on_board < self.passenger_capacity:
                self.passengers_on_board = passengers_on_board
        except ValueError:
            raise TypeError(f"Превышен лимит пассажиров. Вместимость {self.passengers_on_board} пассажиров")

    @property
    def passenger_capacity(self):
        return self._passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, value):
        Airplane.check_number(value)
        self._passenger_capacity = value

    def __str__(self):
        return f"Модель: {self.model_airplane}\n" \
               f"Тип: {self.type_airplane}\n" \
               f"Вместимость пассажиров всего: {self.passenger_capacity}\n" \
               f"Пассажиров на борту: {self.passengers_on_board}"

    @classmethod
    def check_number(cls, num: int):
        if not isinstance(num, int) and num > 0:
            raise TypeError("Петербуржца видно сразу. Пассажиры должны быть целым числом и больше 0")

    def __add__(self, other: int):
        Airplane.check_number(other)
        if self.passengers_on_board + other > self.passenger_capacity:
            raise ValueError("Превышен лимит пассажиров")
        return self.passengers_on_board + other

    def __iadd__(self, other: int) -> int:
        Airplane.check_number(other)
        if self.passengers_on_board + other > self.passenger_capacity:
            raise ValueError("Превышен лимит пассажиров")
        return self.passengers_on_board + other

    def __sub__(self, other: int) -> int:
        Airplane.check_number(other)
        if self.passengers_on_board - other < 0:
            raise ValueError("Пассажиров на борту не может быть меньше 0")
        return self.passengers_on_board - other

    def __isub__(self, other: int) -> int:
        Airplane.check_number(other)
        if self.passengers_on_board - other < 0:
            raise ValueError("Пассажиров на борту не может быть меньше 0")
        return self.passengers_on_board - other

    def __eq__(self, other) -> bool:
        return self.type_airplane == other.type_airplane

    def __lt__(self, other) -> bool:
        return self.passenger_capacity < other.passenger_capacity

    def __le__(self, other) -> bool:
        return self.passenger_capacity <= other.passenger_capacity

    def __gt__(self, other) -> bool:
        return self.passenger_capacity > other.passenger_capacity

    def __ge__(self, other) -> bool:
        return self.passenger_capacity >= other.passenger_capacity


class Flat:
    """ Создать класс Flat (квартира).
    Реализовать перегруженные операторы:
    ■ Проверка на равенство площадей квартир (операция ==);
    ■ Проверка на неравенство площадей квартир (операция !=);
    ■ Сравнение двух квартир по цене (операции > < <= >=).
    """

    def __init__(self, area_flat: int | float, price_flat: int | float):
        self.area_flat = area_flat
        self.price_flat = price_flat

    def __str__(self):
        return f"Жилая площадь квартиры: {self.area_flat}м²\n" \
               f"Стоимость квартиры: {self.price_flat:,}₽"

    def __eq__(self, other) -> bool:
        return self.area_flat == other.area_flat

    def __ne__(self, other) -> bool:
        return self.area_flat != other.area_flat

    def __lt__(self, other) -> bool:
        return self.price_flat < other.price_flat

    def __le__(self, other) -> bool:
        return self.price_flat <= other.price_flat

    def __gt__(self, other) -> bool:
        return self.price_flat > other.price_flat

    def __ge__(self, other) -> bool:
        return f"{self.price_flat}₽ >= {other.price_flat}₽ -> {self.price_flat >= other.price_flat}"


if __name__ == "__main__":
    while (user_log := input("1 class Circle\n"
                             "2 class Complex\n"
                             "3 class  Airplane\n"
                             "4 class Flat\n"
                             "0\n"
                             ": ")) != '0':
        match user_log:
            case '1':
                print('*' * 50)
                circle_20 = Circle(20)
                circle_30 = Circle(30.3)
                list_circle = [circle_20, circle_30]
                for i in list_circle:
                    print(repr(i))
                    print(i)
                print(circle_20 == circle_30)
                print(circle_20 < circle_30)
                print(circle_30 > circle_20)
                print(circle_30 >= circle_20)
                print(circle_30 <= circle_20)
                circle_50 = Circle(50)
                circle_20 + 10
                circle_30 - 15
                print(circle_20)
                print(circle_30)
                print(circle_50)
                print('*' * 50)
            case '2':
                print('*' * 50)
                comp_1 = Complex(1, 2)
                print(repr(comp_1))
                print(f'comp_1 = {comp_1}')
                comp_2 = Complex(2, 4)
                print(f'comp_2 = {comp_2}')
                comp_3 = comp_1 + comp_2
                print(f'{comp_1} + {comp_2} = {comp_3}')
                comp_4 = comp_3 * comp_2
                print(f'{comp_3} * {comp_2} = {comp_4}')
                comp_5 = Complex(2, 3)
                comp_6 = Complex(1, 2)
                comp_7 = comp_5 / comp_6
                print(f'{comp_5} / {comp_6} = {comp_7}')
                print('*' * 50)
                comp_8 = Complex(-3, -9)
                print(comp_8)
                print('*' * 50)
                comp_9 = Complex(3, 9)
                print(comp_9)
                print('*' * 50)

            case '3':
                print('*' * 50)
                tu_154 = Airplane("TU-154", "passenger", 175)
                print(tu_154)
                print('*' * 50)
                tu_154.passengers_on_board += 30
                print(tu_154)
                print('*' * 50)
                tu_154 - 30
                tu_154.passengers_on_board = tu_154 + 70
                print(tu_154)
                print('*' * 50)
                il_76 = Airplane("IL-76", "passenger", 225)
                print(il_76)
                print('*' * 50)
                il_76.passengers_on_board += 150
                print(il_76)
                print('*' * 50)
                print(tu_154)
                print(tu_154 == il_76)
                print('*' * 50)
            case '4':
                my_flat = Flat(95, 10000000)
                print(my_flat)
                print('*' * 50)
                new_flat = Flat(110, 10000000)
                print(new_flat)
                print('*' * 50)
                print(my_flat == new_flat)
                print(my_flat != new_flat)
                print(my_flat < new_flat)
                print(my_flat <= new_flat)
                print(my_flat > new_flat)
                print(my_flat >= new_flat)

            case _:
                print("Пропустим.")
                print('*' * 50)
