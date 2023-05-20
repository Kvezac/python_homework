from csv import DictReader, DictWriter


class Recipe:
    def __init__(self, name_recipe: str, author: str, type: str, description: str, video_link: str,
                 ingredients: [str], kitchen: str):
        self.name_recipe = name_recipe
        self.author = author
        self.type = type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.kitchen = kitchen

    def __str__(self):
        return ', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])


class Model:
    def __init__(self, filename):
        self.filename = filename
        self.database = []
        try:
            with open(self.filename, newline='') as csvfile:
                data = DictReader(csvfile)
                for row in data:
                    self.database.append(
                        Recipe(row['name_recipe'], row['author'],
                               row['type'], row['description'],
                               row['video_link'], row['ingredients'],
                               row['kitchen']))
        except FileNotFoundError:
            print('Error in loading database. Proceed with empty data.')

    def __to_dict__(self):
        pass

    def __save_data__(self):
        with open('save_test.csv', 'w', encoding='utf-8', newline='') as csv_save:
            fields_name = ['name_recipe', 'author', 'type', 'description', 'video_link', 'ingredients', 'kitchen']
            data_writer = DictWriter(csv_save, fieldnames=fields_name, quotechar='"', delimiter=',',
                                     skipinitialspace=True)
            data_writer.writeheader()
            for rec in self.database:
                data_writer.writerow(rec.__dict__)

    def add_recipe(self, recipe_data):
        self.database.append(Recipe(*recipe_data))
        self.__save_data__()

    def get_recipes(self,words):
        words = list(map(str.strip, words.split(',')))
        recipes = []
        for word in words:
            print('1', word)
            for recipe in self.database:
                print(recipe)
                if word in ' '.join(map(str, recipe.__dict__.values())) and recipe not in recipes:
                    recipes.append(recipe)
            return recipes

    def remove_recipe(self, recipe):
        self.database.remove(recipe)
        self.__save_data__()


if __name__ == '__main__':
    m = Model('database.csv')
    m.database
    [print(i, sep=', ') for i in m.database]
    m.__save_data__()
