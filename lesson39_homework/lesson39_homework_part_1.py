"""Создайте программу Python для интернет-магазина, состоящую из двух основных классов: CustomerManager и
ProductInventory. Класс CustomerManager должен отвечать за обработку операций, связанных с клиентами,
таких как добавление новых клиентов, обновление информации о клиентах и получение данных о клиентах. Он должен иметь
такие методы, как add_customer(), update_customer() и get_customer(). Класс ProductInventory должен отвечать за
управление запасами товаров в магазине. Он должен обрабатывать такие операции, как добавление продуктов, обновление
информации о продукте и получение сведений о продукте. Он должен иметь такие методы, как add_product(),
update_product() и get_product(). Разделяя управление клиентами и запасами продуктов на отдельные классы,
вы гарантируете, что каждый класс несет единую ответственность, делая программу более модульной и простой в
обслуживании."""


class CustomerManager:
    customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def update_customer(self, customer_id, updated_info):
        for customer in self.customers:
            if customer['id'] == customer_id:
                customer.update(updated_info)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer['id'] == customer_id:
                return customer


class ProductInventory:
    products = []

    def add_product(self, product):
        self.products.append(product)

    def update_product(self, product_id, updated_info):
        for product in self.products:
            if product['id'] == product_id:
                product.update(updated_info)

    def get_product(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                return product


if __name__ == '__main__':
    # Пример использования классов
    customer_manager = CustomerManager()
    product_inventory = ProductInventory()
    customer_manager.add_customer({
        'id': 1,
        'name': 'Andrey',
        'email': 'Andrey@example.com'

    })
    customer_manager.add_customer({
        'id': 2,
        'name': 'Sasha',
        'email': 'Sasha@example.com'

    })
    product_inventory.add_product({
        'id': 1,
        'name': 'Phone',
        'price': 1000})
    product_inventory.add_product({
        'id': 2,
        'name': 'TV',
        'price': 1200})
    customer_manager.update_customer(1, {'email': 'Andrey@example.com'})
    customer_manager.update_customer(2, {'email': 'Sasha@example.com'})
    product_inventory.update_product(1, {'price': 2000})
    product_inventory.update_product(2, {'price': 1000})

    print(customer_manager.get_customer(1))
    print(customer_manager.get_customer(2))
    print(product_inventory.get_product(1))
    print(product_inventory.get_product(2))
