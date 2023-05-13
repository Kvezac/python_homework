from abc import ABC, abstractmethod
from random import randint


class NumberFacade:
    """ Есть класс, предоставляющий доступ к набору чисел.
        Источником этого набора чисел является некоторый
        файл. С определенной периодичностью данные в файле
        меняются (надо реализовать механизм обновления).
        Приложение должно получать доступ к этим данным и
        выполнять набор операций над ними (сумма, максимум,
        минимум и т.д.). При каждой попытке доступа к этому
        набору необходимо вносить запись в лог-файл. При
        реализации используйте паттерн Proxy (для логирования)
        и другие необходимые паттерны.
    """

    def __init__(self, file_name: str):
        self._number_action = NumberActionRead(file_name)

    def get_sum(self) -> int:
        return self._number_action.get_sum()

    def get_max(self) -> int:
        return self._number_action.get_max()

    def get_min(self) -> int:
        return self._number_action.get_min()


class NumberAction(ABC):
    @abstractmethod
    def get_numbers(self) -> list[int]:
        pass

    def get_sum(self) -> int:
        result = sum(self.get_numbers())
        self.log_operation(f"Sum: {result}")
        return result

    def get_max(self) -> int:
        result = max(self.get_numbers())
        self.log_operation(f"Max: {result}")
        return result

    def get_min(self) -> int:
        result = min(self.get_numbers())
        self.log_operation(f"Min: {result}")
        return result

    def log_operation(self, message: str):
        with open("log.txt", "a", encoding="UTF-8") as f:
            print(message, file=f)
            print("-" * 10, file=f)


class NumberActionProxy(NumberAction):
    def __init__(self, file_name: str):
        self._number_action = NumberActionRead(file_name)

    def get_numbers(self) -> list[int]:
        return self._number_action.get_numbers()


class NumberActionRead(NumberAction):

    def __init__(self, file_name: str):
        self._file_name = file_name

    def get_numbers(self) -> list[int]:
        with open(self._file_name, "r", encoding="UTF-8") as f:
            data = f.read()
            numbers = [int(line.strip()) for line in data.split()]
            return numbers


class FileUpdater:
    def __init__(self, file_mame: str):
        self._file_name = file_mame
        self._number_action = [randint(0, 300) for _ in range(randint(3, 100))]

    def update_file(self):
        with open(self._file_name, "w", encoding="UTF-8") as f:
            f.write(" ".join(map(str, self._number_action)))


if __name__ == '__main__':
    file_name = "numbers.txt"
    file_updater = FileUpdater(file_name)
    file_updater.update_file()
    number_facade = NumberFacade(file_name)
    while (user_log := input("Choose a command to execute:\n"
                             "1 Get sum\n"
                             "2 Get max\n"
                             "3 Get min\n"
                             "4 Update list numbers\n"
                             "0 Exit\n: ")) != '0':
        match user_log:
            case "1":
                print('sum:', number_facade.get_sum())

            case "2":
                print('max:', number_facade.get_max())

            case "3":
                print('min:', number_facade.get_min())

            case "4":
                file_updater = FileUpdater(file_name)
                file_updater.update_file()

            case _:
                print("There is no command like this.")
    print("Program finish.")
