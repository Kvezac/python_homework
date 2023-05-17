class View:
    def wait_user_answer(self):
        new_line = '\n'
        menu_items = [" MENU SHOES ".center(50, '='),
                      '1. Adding new shoes',
                      '2. All shoes',
                      '3. Shoes search',
                      '4. Shoes delete size',
                      '"Quit". Close program.',
                      ': ']
        query = input(f'{new_line.join(menu_items)}')
        return query

    def add_new_shoes(self):
        dict_shoes = {'gender': None,
                      'type': None,
                      'manufacturer': None,
                      'size': None,
                      'color': None,
                      'price': None}

        for key in dict_shoes.keys():
            dict_shoes[key] = input(f'Input {key.lower()}: ')
        dict_shoes['size'] = [str(i) for i in dict_shoes['size'].split(', ')]
        return dict_shoes

    def __throw_an_error__(self, error):
        print('Some error has occurred:', error)

    def print_shoes(self, shoes):
        if isinstance(shoes, list):
            [print(str(ind).center(4, ' ').center(50, '='), value, sep='\n') for ind, value in enumerate(shoes, 1)]
        else:
            print('Edit your search query.')

    def shoes_search(self):
        criteria = input("Enter a list of words separated by a space: ").split()
        return criteria

    def get_gender(self):
        while (gender_inp := input('1. male\n'
                                   '2. female\n'
                                   '3. unisex\n: ')):
            match gender_inp:
                case '1':
                    return 'male'
                case '2':
                    return 'female'
                case '3':
                    return 'unisex'
                case _:
                    print("There is no command like this.")

    def get_number_model(self):
        number = int(input("Input number shoes for delete: "))
        return number

    def get_size_model(self):
        number_ind = int(input("input size shoes: "))
        return number_ind

    def return_delete_result(self, result):
        print(result)


if __name__ == '__main__':
    v = View()
    print(v.get_gender())
