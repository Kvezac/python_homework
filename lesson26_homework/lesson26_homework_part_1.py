from abc import ABC, abstractmethod


class Figure(ABC):
    """  Часть 1:
        Создать базовый класс Фигура с методом для подсчета
        площади. Создать производные классы: прямоугольник,
        круг, прямоугольный треугольник, трапеция со своими
        методами для подсчета площади.
         Часть 2:
        Для классов из задания 1 нужно переопределить
        магические методы:
         int(возвращает площадь)
         str(возвращает информацию о фигуре).
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    def __int__(self) -> int:
        return int(self.area)

    def __str__(self) -> str:
        return f'Фигура: {self.name}\n' \
               f'{self.get_info}\n' \
               f'Площадь: {self.area}'


class RectangleA(Figure):

    def __init__(self, height: int | float, width: int | float):
        Figure.__init__(self, 'Прямоугольник')
        self.height = height
        self.width = width

    @property
    def get_info(self) -> str:
        return f'Высота: {self.height}\n' \
               f'Ширина: {self.width}'

    @property
    def area(self) -> int | float:
        return self.height * self.width


class CircleA(Figure):

    def __init__(self, radius: int | float):
        Figure.__init__(self, 'Круг')
        self.radius = radius

    @property
    def get_info(self) -> str:
        return f'Радиус: {self.radius}'

    @property
    def area(self) -> int | float:
        return self.radius ** 2 * 3.14


class RightTriangle(Figure):

    def __init__(self, leg_1: int | float, leg_2: int | float):
        Figure.__init__(self, 'Прямоугольный треугольник')
        self.leg_1 = leg_1
        self.leg_2 = leg_2

    @property
    def get_info(self) -> str:
        return f'Катет 1: {self.leg_1}\n' \
               f'Катет 2: {self.leg_2}'

    @property
    def area(self) -> int | float:
        return self.leg_1 * self.leg_2 / 2


class Trapeze(Figure):
    def __init__(self, long: int | float, short: int | float, height: int | float):
        Figure.__init__(self, 'Трапеция')
        self.long = long
        self.short = short
        self.height = height

    @property
    def get_info(self) -> str:
        return f'Длина более длинного основания: {self.long}\n' \
               f'Длина меньшего основания: {self.short}\n' \
               f'Высота трапеции: {self.height}'

    @property
    def area(self) -> int | float:
        return (self.short + self.long) / 2 + self.height


class Shape(ABC):
    """ Создайте базовый класс Shape для рисования плоских
       фигур.
        Определите методы:
       ■ Show() — вывод на экран информации о фигуре;
       ■ Save() — сохранение фигуры в файл;
       ■ Load() — считывание фигуры из файла.
        Определите производные классы:
       ■ Square — квадрат, который характеризуется координатами левого
         верхнего угла и длиной стороны;
       ■ Rectangle — прямоугольник с заданными координатами верхнего
         левого угла и размерами сторон;
       ■ Circle — окружность с заданными координатами центра и радиусом;
       ■ Ellipse — эллипс с заданными координатами верхнего
         угла описанного вокруг него прямоугольника со сторонами,
         параллельными осям координат, и размерами этого прямоугольника.
       Создайте список фигур, сохраните фигуры в файл,
       загрузите в другой список и отобразите информацию о
       каждой из фигур
    """
    shape_list = []

    def __init__(self, name: str, x: int | float = 0, y: int | float = 0):
        self.name = name
        self.x = x
        self.y = y
        Shape.shape_list.append([self.__class__.__name__, self.name, self.x, self.y, self.get_info])
        Shape.save()

    @abstractmethod
    def get_info(self):
        pass

    def show(self):
        return f'{self.name}\n' \
               f'{self.get_info}\n' \
               f'Координаты начало отсчета:\n' \
               f'x = {self.x}\n' \
               f'y = {self.y}'

    @classmethod
    def save(cls):
        with open('shape.txt', 'w', encoding='utf-8') as f:
            for line in cls.shape_list:
                print(line, file=f)
            f.flush()

    @classmethod
    def load(cls):
        with open('shape.txt', 'r', encoding='utf-8') as f:
            new_list = []
            for line in f:
                new_list.append(line.strip())
        return new_list


class Square(Shape):

    def __init__(self, x: int | float, y: int | float, height: int | float):
        self.height = height
        Shape.__init__(self, "Квадрат", x, y)

    @property
    def get_info(self) -> str:
        return self.height


class Circle(Shape):

    def __init__(self, x: int | float, y: int | float, radius: int | float):
        self.radius = radius
        Shape.__init__(self, "Окружность", x, y)

    @property
    def get_info(self) -> str:
        return self.radius


class Ellipse(Shape):

    def __init__(self, x: int | float, y: int | float, height: int | float, width: int | float):
        self.height = height
        self.width = width
        Shape.__init__(self, 'Эллипс', x, y)

    @property
    def get_info(self) -> str:
        return self.height, self.width


if __name__ == "__main__":
    while (user_log := input("1 class Figure\n"
                             "2 class Shape\n"
                             "0 Выход\n"
                             ": ")) != '0':
        match user_log:
            case '1':
                rectangle = RectangleA(20, 40)
                print(rectangle)
                print(f'Инт: {int(rectangle)}')
                print("*" * 50)
                circle = CircleA(30)
                print(circle)
                print(f'Инт: {int(circle)}')
                print("*" * 50)
                right_triangle = RightTriangle(40, 70)
                print(right_triangle)
                print(f'Инт: {int(right_triangle)}')
                print("*" * 50)
                trapeze = Trapeze(50, 30, 10)
                print(trapeze)
                print(f'Инт: {int(trapeze)}')
                print("*" * 50)
            case "2":
                my_square = Square(10, 30, 40)
                print(my_square.show())
                print("*" * 50)
                my_circle = Circle(-1, 17, 90)
                print(my_circle.show())
                print("*" * 50)
                my_ellipse = Ellipse(-20, -40, 200, 100)
                print(my_ellipse.show())
                print("*" * 50)
                file = Shape.load()
                for i in file:
                    i = i.strip('[]').split()
                    print(f"класс: {i[0]}\n"
                          f"имя: {i[1]}\n"
                          f"координаты начала отсчета: x = {i[2]}, y = {i[3]}\n"
                          f"Размер: {i[4:]}")
                    print("*" * 50)

            case _:
                print("Попробуем еще раз.")
