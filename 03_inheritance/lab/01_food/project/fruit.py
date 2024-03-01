from project.food import Food

class Fruit(Food):
    def __init__(self, name, experation_date):
        self.name = name
        super().__init__(experation_date)