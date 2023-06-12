"""Создайте программу Python, определяющую иерархию классов для различных геометрических фигур, таких как Shape,
Circle, Rectangle и Triangle. Класс Shape должен служить базовым классом, предоставляя общие свойства и методы для
всех фигур. Каждый конкретный класс формы (Circle, Rectangle, Triangle) должен наследоваться от Shape и реализовывать
свои собственные методы, такие как calculate_area() и calculate_perimeter(). Программа должна позволять вам
рассматривать любую фигуру как экземпляр класса Shape, обеспечивая соблюдение принципа подстановки Лисков. Это
означает, что вы должны иметь возможность заменить любую конкретную фигуру объектом Shape в любой части программы,
не влияя на её выполнение. Разрабатывая иерархию классов в соответствии с принципом замещения Лискова, вы создаете
систему, которая является более гибкой, расширяемой и способной единообразно обрабатывать операции, связанные с
формами."""

import math


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


if __name__ == '__main__':
    circle = Circle(5)
    print("Area of circle:", circle.calculate_area())
    print("Perimeter of circle:", circle.calculate_perimeter())

    rectangle = Rectangle(3, 4)
    print("Area of rectangle:", rectangle.calculate_area())
    print("Perimeter of rectangle:", rectangle.calculate_perimeter())

    triangle = Triangle(3, 4, 5)
    print("Area of triangle:", triangle.calculate_area())
    print("Perimeter of triangle:", triangle.calculate_perimeter())

    shapes = [circle, rectangle, triangle]
    for shape in shapes:
        print("Area of shape:", shape.calculate_area())
        print("Perimeter of shape:", shape.calculate_perimeter())