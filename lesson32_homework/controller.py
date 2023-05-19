from model import Model
from view import View

class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model('test_database.csv')

    def run(self):
        query = None
        while query != 'Quit':
            query = self.view.wait_user_answer()
            self.user_response_answer(query)

    def user_response_answer(self, query):
        if query == '1':
            target = self.view.get_target()
            self.model.add_recipe(target)
