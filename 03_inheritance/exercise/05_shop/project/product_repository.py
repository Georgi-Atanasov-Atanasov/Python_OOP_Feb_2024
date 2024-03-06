from project.drink import Drink
from project.food import Food

class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self,product):
        self.products.append(product)

    def find(self,product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        if product_name in self.products:
            self.products.remove(product_name)

    def __repr__(self):
        return '\n'.join(f"{x.name}: {x.quantity}" for x in self.products)


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
