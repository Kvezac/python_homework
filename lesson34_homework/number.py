class Number:
    """ Создайте класс для числа. В классе должна быть реализована следующая функциональность:
         ■ Запись и чтение значения.
         ■ Перевод числа в восьмеричную систему исчисления.
         ■ Перевод числа в шестнадцатеричную систему исчисления.
         ■ Перевод числа в двоичную систему исчисления.
        Протестируйте все возможности созданного класса
        с помощью модульного тестирования(unittest)
    """

    def __init__(self, number: int):
        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        if isinstance(value, int):
            self._number = value

    def __str__(self):
        return str(self._number)

    @staticmethod
    def num_convector(num: int, base: int):
        if num == 0:
            return '0'
        digits = '0123456789ABCDEF'
        num_conv = ''
        while num > 0:
            num_conv = digits[num % base] + num_conv
            num //= base
        return num_conv

    @property
    def number_to_oct(self):
        return f'0o{self.num_convector(self._number, 8)}'

    @property
    def number_to_hex(self):
        return f'0x{self.num_convector(self._number, 16)}'

    @property
    def number_to_bin(self):
        return f'0b{self.num_convector(self._number, 2)}'


if __name__ == '__main__':
    num = Number(22)
    num.number = '1'
    print(num)
    # print(num)
    # print(num.number_to_bin)  # 0b10110
    # print(num.number_to_hex)  # 0x16
    # print(num.number_to_oct)  # 0o26
    # num.number = 0
    # print(num)
    # print(num.number_to_bin)  # 0b1010
    # print(num.number_to_hex)  #
    # print(num.number_to_oct)  # 0o26
    # print(num)
    # num.number = -15
    # print(num)
    # print(num.number_to_bin)  # 0b1010
    # print(num.number_to_hex)  #
    # print(num.number_to_oct)  # 0o26

