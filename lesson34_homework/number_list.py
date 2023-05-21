from random import randint, seed

seed(0)


class NumberList:
    """" Создайте класс, содержащий набор целых чисел.
         В классе должна быть реализована следующая функциональность:
          ■ Сумма элементов набора.
          ■ Среднеарифметическое элементов набора.
          ■ Максимум из элементов набора.
          ■ Минимум из элементов набора.
         Протестируйте все возможности созданного класса
         с помощью модульного тестирования(unittest)
    """

    def __init__(self):
        self.__numbers_list = NumberList._numbers_list()

    @staticmethod
    def _numbers_list():
        return [randint(1, 100) for _ in range(10)]

    def update_numbers_list(self):
        self.__numbers_list = NumberList._numbers_list()

    def get_sum(self) -> int | float:
        result = sum(self.__numbers_list)
        return result

    def get_avg(self):
        result = self.get_sum() / len(self.__numbers_list)
        return result

    def get_max(self) -> int | float:
        result = max(self.__numbers_list)
        return result

    def get_min(self) -> int | float:
        result = min(self.__numbers_list)
        return result

    def __str__(self):
        return f'{self.__numbers_list}'


if __name__ == '__main__':
    n = NumberList()
    print(n.get_sum())
    print(n.get_avg())
    print(n.get_max())
    print(n.get_min())
    n.update_numbers_list()
    print(n.get_sum())
    print(n.get_avg())
    print(n.get_max())
    print(n.get_min())

