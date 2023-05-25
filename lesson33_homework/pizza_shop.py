from time import localtime, strftime

from abc import ABC, abstractmethod


class PizzaBase(ABC):
    @abstractmethod
    def cost(self):
        return


class PizzaBase25cm(PizzaBase):
    @property
    def cost(self):
        return 8

    def __str__(self):
        return f'основа для пиццы 25 см'


class PizzaBase30cm(PizzaBase):
    @property
    def cost(self):
        return 9

    def __str__(self):
        return f'основа для пиццы 30 см'


class Toppings:
    data_toppings = {'tomato_sauce': {'name': 'томатный соус', 'cost': 12},
                     'mozzarella': {'name': 'моцарелла', 'cost': 10},
                     'pepperoni': {'name': 'пепперони', 'cost': 15},
                     'ham': {'name': 'ветчина', 'cost': 15},
                     'pineapple': {'name': 'ананас', 'cost': 10},
                     'mushrooms': {'name': 'грибы', 'cost': 15},
                     'peppers': {'name': 'перец', 'cost': 10},
                     'onions': {'name': 'лук', 'cost': 15},
                     'sausage': {'name': 'колбаса', 'cost': 10},
                     'basil': {'name': 'базилик', 'cost': 10}}

    toppings = {}

    @staticmethod
    def init_toppings():
        for key, value in Toppings.data_toppings.items():
            Toppings.toppings[key] = type(key.title().replace('_', ''), (PizzaBase,), value)


class Pizzas:
    Toppings.init_toppings()
    data_pizzas = {'margherita': {'name': 'маргарита',
                                  'toppings': [Toppings.toppings[top] for top in ['tomato_sauce', 'mozzarella',
                                                                                  'basil']],
                                  'base': PizzaBase25cm()
                                  },
                   'pepperoni': {'name': 'пепперони',
                                 'toppings': [Toppings.toppings[top] for top in
                                              ['tomato_sauce', 'mozzarella', 'basil']],
                                 'base': PizzaBase25cm()},
                   'hawaiian': {'name': 'гавайская',
                                'toppings': [Toppings.toppings[top] for top in ['tomato_sauce', 'mozzarella',
                                                                                'ham', 'pineapple']],
                                'base': PizzaBase25cm()},
                   'vegetarian': {'name': 'вегетарианская',
                                  'toppings': [Toppings.toppings[top] for top in ['tomato_sauce', 'mozzarella',
                                                                                  'mushrooms', 'peppers', 'onions']],
                                  'base': PizzaBase25cm()},
                   'meat_lovers': {'name': 'мясная',
                                   'toppings': [Toppings.toppings[top] for top in ['tomato_sauce', 'mozzarella',
                                                                                   'pepperoni', 'sausage', 'ham']],
                                   'base': PizzaBase25cm()}

                   }
    pizzas = {}

    @staticmethod
    def init_pizzas():
        for key, value in Pizzas.data_pizzas.items():
            Pizzas.pizzas[key] = type(key.title().replace("_", ""), (PizzaBase,), value)


class Menu:
    @staticmethod
    def show_menu_pizzas(pizzas):
        for ind, pizza in enumerate(pizzas.items(), 1):
            name_pizza = pizza[1].name
            base_pizza = pizza[1].base
            topping = [top.name for top in pizza[1].toppings]
            price = sum(top.cost for top in pizza[1].toppings) * pizza[1].base.cost
            print(f'{ind}. {name_pizza.title()}: {base_pizza}({", ".join(topping)}), Цена: {price}₽')

    @staticmethod
    def show_menu_toppings(toppings):
        print('Топинги:')
        for ind, top in enumerate(toppings.items(), 1):
            name_top = top[1].name
            price = top[1].cost
            print(f'{ind}. {name_top}, Цена: {price}')

    @staticmethod
    def show_basket(basket):
        total = 0
        for ind, value in enumerate(basket, 1):
            name_pizza = value.name
            base_pizza = value.base
            topping = [top.name for top in value.toppings]
            price = sum(top.cost for top in value.toppings) * value.base.cost
            total += price
            print(f'{ind}. {name_pizza.title()}: {base_pizza}({", ".join(topping)}), Цена: {price}₽')
        print(f'Сумма заказа {total}₽')


class SaveOrder:
    def __init__(self, order, amount, pay, file_name='database_pizza.txt'):
        self.file_name = file_name
        self.order = order
        self.amount = amount
        self.pay = pay

    def save(self):
        with open(self.file_name, 'a', encoding='utf-8') as f:
            save_line = f'{strftime("%d.%m.%Y %H:%M:%S", localtime())} '
            for value in self.order:
                save_line += f'{value.name} '
            save_line += f'{self.pay.lower()} {str(self.amount).lower()}'
            print(save_line, file=f)


class Payment:
    @staticmethod
    def do_transaction(amount):
        raise NotImplementedError


class Cash(Payment):
    @staticmethod
    def do_transaction(amount):
        return f'Заказ оплачен наличными'


class BankCard(Payment):
    @staticmethod
    def do_transaction(amount):
        return f'Заказ оплачен банковской картой'


class Pizzeria:
    def __init__(self):
        self.sold_pizzas = 0  # количество проданных пицц
        self.revenue = 0  # доход
        self.profit = 0  # прибыль
        self.basket = []
        Toppings.init_toppings()
        Pizzas.init_pizzas()

    def run(self):
        while (query := input('1. Добавить пиццу в корзину\n'
                              '2. Удалить пиццу из корзины\n'
                              '3. Просмотреть ваш заказ\n'
                              '4. Очистить корзину\n'
                              '5. Оплатить товары в корзине\n'
                              '6. info'
                              '"Exit". Выход\n: ')).lower() != 'Exit'.lower():
            if query == '1':
                self.add_pizza()

            elif query == '2':
                self.remove_pizza()

            elif query == '3':
                self.show_basket()

            elif query == '4':
                self.clear_basket()

            elif query == '5':
                self.do_payment()

            elif query == '6':
                self.info()

        print('Ждём вас снова. ')

    def info(self):
        print(f'Количество оплаченных пицц: {self.sold_pizzas} шт.\n'
              f'Доход: {self.revenue}₽\n'
              f'Прибыль: {self.profit:.2f}₽')

    def total(self, pizza):
        self.sold_pizzas += 1
        price = sum(top.cost for top in pizza.toppings) * pizza.base.cost
        self.revenue += price
        self.profit += (60 * price) / 100
        return price

    def do_payment(self):
        payment = (Cash, BankCard)[int(input('1. Наличные.\n'
                                             '2. Банковской картой\n'
                                             'Выберите способ оплаты\n: ')) - 1]
        amount = sum([self.total(i) for i in self.basket])
        date = payment.do_transaction(amount)
        base = SaveOrder(self.basket, amount, date)
        base.save()
        print(f'{date}. Сумма заказа {amount}₽')
        self.clear_basket()

    def add_topping(self, pizza):
        Menu.show_menu_toppings(Toppings.toppings)
        while (query := input('Выберите опцию:\n'
                              'Введите номер топинга, который вы бы хотели добавить\n'
                              '"q". Не добавлять топинг\n: ')) != 'q':
            try:
                order = Toppings.toppings[list(Toppings.toppings)[int(query) - 1]]
                pizza.toppings.append(order)
                print(pizza.__dict__.items())
            except ValueError:
                print('Введите число значение')
            except IndexError:
                print('Топинга не  существует.')
            Menu.show_menu_toppings(Toppings.toppings)

    def remove_pizza(self):
        Menu.show_basket(self.basket)
        request = input('Введите номер пиццы, которую вы бы хотели удалить из корзины\n: ')
        try:
            self.basket.pop(int(request) - 1)
        except IndexError:
            print('Не правильно выбран номер.')

    def clear_basket(self):
        self.basket.clear()

    def make_an_order(self, value):
        self.basket.append(value)
        print(f'Пицца: {value.name.title()} добавлена в корзину')

    def show_basket(self):
        print('Ваша корзина:')
        Menu.show_basket(self.basket)

    def add_pizza(self):
        while (query := input('Выберите опцию:\n'
                              '1. Выбрать одну из готовых пицц\n'
                              '2. Собрать пиццу самому\n'
                              'q. Выход в главное меню\n: ')) != 'q':
            if query == '1':
                Menu.show_menu_pizzas(Pizzas.pizzas)
                request = input('Введите номер пиццы, которую вы бы хотели заказать\n: ')
                order = Pizzas.pizzas[list(Pizzas.pizzas)[int(request) - 1]]
                order.base = PizzaBase25cm()
                size = input('Введите размер пиццы(25 / 30)\n: ')
                if size == '30':
                    order.base = PizzaBase30cm()
            elif query == '2':
                base = [PizzaBase25cm(), PizzaBase25cm()]
                for ind, dough in enumerate(base, 1):
                    print(f'{ind}. {dough}')
                date = input('Выберите основу для вашей пиццы\n: ')
                order = type('user', (PizzaBase,), {'name': 'user', 'toppings': [], 'base': base[int(date) - 1]})
            self.add_topping(order)
            self.make_an_order(order)


if __name__ == '__main__':
    app = Pizzeria()
    app.run()
