class View:
    def wait_user_answer(self):
        print(' Waiting for user input. '.center(50, '-'))
        print('1. Add new recipe\n'
              '2. Get recipe by filter\n'
              '3. Remove recipe\n'
              '"Quit" Exit the program.')
        result = input(': ')
        return result

    def get_recepi_data(self):
        properties = ['name recipe', 'author', 'type', 'description', 'video link', 'ingredients', 'kitchen']
        row_data = [input(f'Input {value.title()}: ') for value in properties]
        return row_data

    def get_target(self):
        words = input('Input keywords to find films, comma separated: ')
        return words

    def print_recipe(self, recipes):
        [print(f'{ind}. {recipe}') for ind, recipe in enumerate(recipes, 1)]



if __name__ == '__main__':
    v = View()
    v.get_recepi_data()