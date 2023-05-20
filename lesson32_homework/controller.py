from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model('database.csv')

    def run(self):
        query = None
        while query != 'Quit':
            query = self.view.wait_user_answer()
            self.user_response_answer(query)

    def user_response_answer(self, query):
        if query == '1':
            target = self.view.get_recepi_data()
            self.model.add_recipe(target)

        elif query == '2':
            target = self.view.get_target()
            recipes = self.model.get_recipes(target)
            self.view.print_recipe(recipes)

        elif query == '3':
            target = self.view.get_target()
            recipes = self.model.get_recipes(target)
            if len(recipes) > 1:
                number = self.view.delition_context(recipes)
                recipes = [recipes[number - 1]]
            self.model.remove_recipe(recipes[0])
