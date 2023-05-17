from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def run(self):
        query = None
        while query != 'Quit':
            query = self.view.wait_user_answer()
            self.check_user_answer(query)

    def check_user_answer(self, query):
        if query == '1':
            shoes_data = self.view.add_new_shoes()
            self.model.add_new_shoes(shoes_data)
        elif query == '2':
            print('all_list')
            all_shoes = self.model.shoes
            self.view.print_shoes(all_shoes)

        elif query == '3':
            criteria = self.view.shoes_search()
            shoes = self.model.shoes_search(criteria)
            self.view.print_shoes(shoes)

        elif query == '4':
            model_gender = self.view.get_gender().split()
            shoes = self.model.shoes_search(model_gender)
            self.view.print_shoes(shoes)
            try:
                number_model = self.view.get_number_model()
                shoes = [shoes[number_model-1]]
                self.view.print_shoes(shoes)
            except IndexError as e:
                self.view.__throw_an_error__(e)
            size_model = self.view.get_size_model()
            result = self.model.remove_size(*shoes, size_model)
            self.view.return_delete_result(result)


