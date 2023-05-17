import json


class Shoes:
    def __init__(self, gender: str, type: str, manufacturer: str, size: [int | float], color: str, price: int | float):
        self.gender: str = gender
        self.type: str = type
        self.manufacturer: str = manufacturer
        self.size: [int | float] = size
        self.color: str = color
        self.price: str = price

    def __str__(self):
        return f'Type: {self.type}\n' \
               f'Gender: {self.gender}\n' \
               f'Size: {", ".join(self.size)}\n' \
               f'Color: {self.color}\n' \
               f'Price: {self.price}\n' \
               f'{"-" * 50}'


class Model:
    def __init__(self):
        self.filepath = 'test_save.json'
        self.__shoes = []
        self.data = json.load(open(self.filepath, 'r', encoding='utf-8'))
        for value in self.data:
            self.__shoes.append(Shoes(*value.values()))

    @property
    def shoes(self):
        return self.__shoes

    def save_shoes(self):
        dict_shoes = [value.__dict__ for value in self.__shoes]
        json.dump(dict_shoes, open('database.json.json', 'w', encoding='utf-8'), indent=4)

    def add_new_shoes(self, shoes_data):
        new_shoes = Shoes(*shoes_data.values())
        self.__shoes.append(new_shoes)
        self.save_shoes()

    def shoes_search(self, criteria):
        shoes = []
        for shoe in self.__shoes:
            for crit in criteria:
                if shoe in shoes:
                    break
                for prop in shoe.__dict__.values():
                    if not isinstance(prop, list) and crit.lower() == prop.lower():
                        shoes.append(shoe)
                        break
        return shoes

    def remove_size(self, shoes, size):
        shoes.size = [value for value in shoes.size if int(value) != size]
        if len(shoes.size) == 0:
            del shoes
            self.save_shoes()
            return f'No more sizes'
        self.save_shoes()
        return f'Size removed'



if __name__ == '__main__':
    m = Model()
    [print(shoe.type) for shoe in m.shoes]
