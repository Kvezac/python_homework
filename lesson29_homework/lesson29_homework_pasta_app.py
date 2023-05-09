from abc import ABC, abstractmethod


class Pasta:
    """ Создайте приложение для приготовления пасты.
        Приложение должно уметь создавать минимум три вида пасты.
        Классы различной пасты должны иметь следующие методы:
        ■ Тип пасты;
        ■ Соус;
        ■ Начинка;
        ■ Добавки.
        Для реализации используйте порождающие паттерны
    """

    def __init__(self):
        self.type: str = ""
        self.sauce: str = ""
        self.filing: str = ""
        self.toppings: [str] = []

    def set_type(self, pasta_type):
        self.type = pasta_type

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_filling(self, filling):
        self.filing = filling

    def add_toppings(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        string = f"PASTA: {self.type}\n" \
                 f"SAUCE: {self.sauce}\n" \
                 f"FILLING: {self.filing}\n" \
                 f"TOPPINGS:\n"
        for topping in self.toppings:
            string += f"\t{topping}\n"
        return string


class PastaBuilder(ABC):

    def __init__(self):
        self.pasta = Pasta()

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_type(self):
        pass

    @abstractmethod
    def set_sauce(self):
        pass

    @abstractmethod
    def set_filling(self):
        pass

    @abstractmethod
    def add_topping(self):
        pass

    def get_pasta(self):
        return self.pasta


class SpaghettiCarbonaraBuilder(PastaBuilder):

    def reset(self):
        self.pasta = Pasta()

    def set_type(self):
        self.pasta.set_type("Spaghetti")

    def set_sauce(self):
        self.pasta.set_sauce("carbonara")

    def set_filling(self):
        self.pasta.set_filling("-")

    def add_topping(self):
        self.pasta.add_toppings("bacon")


class BolognesePastaBuilder(PastaBuilder):

    def reset(self):
        self.pasta = Pasta()

    def set_type(self):
        self.pasta.set_type("Bolognese")

    def set_sauce(self):
        self.pasta.set_sauce("tomato sauce")

    def set_filling(self):
        self.pasta.set_filling("ground meat")

    def add_topping(self):
        self.pasta.add_toppings("-")


class AlfredoPastaBuilder(PastaBuilder):
    def reset(self):
        self.pasta = Pasta()

    def set_type(self):
        self.pasta.set_type("Fettuccine")

    def set_sauce(self):
        self.pasta.set_sauce("alfredo")

    def set_filling(self):
        self.pasta.set_filling("-")

    def add_topping(self):
        self.pasta.add_toppings("parmesan cheese")


class Director:

    def __init__(self, builder):
        self.builder = builder

    def make_pasta(self):
        self.builder.set_type()
        self.builder.set_sauce()
        self.builder.set_filling()
        self.builder.add_topping()

    def get_pasta(self):
        return self.builder.get_pasta()


if __name__ == '__main__':
    while (user_inp := input("Choose a command to execute:\n"
                             "1 Spaghetti\n"
                             "2 Bolognese\n"
                             "3 Fettuccine\n"
                             "q Exit\n: ")) != 'q':
        spaghetti = None
        if user_inp not in ['1', '2', '3']:
            print("There is no command like this!")
            continue
        elif user_inp == '1':
            spaghetti = SpaghettiCarbonaraBuilder()
        elif user_inp == '2':
            spaghetti = BolognesePastaBuilder()
        elif user_inp == '3':
            spaghetti = AlfredoPastaBuilder()

        pasta = Director(spaghetti)
        pasta.make_pasta()
        print("*" * 50)
        print(pasta.get_pasta())
        print("-" * 50)
    print("End of program.")
