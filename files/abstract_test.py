from abc import ABC, abstractmethod

class Food(ABC):
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    @abstractmethod
    def apply_discount(self):
        pass

    def display_details(self):
        disc_price = self.price - self.apply_discount()
        print (f"Name: {self.name}\nCategory: {self.category}\nOriginal Price: {self.price}\nDiscounted Price: ${disc_price}\n")

class MainCourse(Food):
    def __init__(self,name, price, serving_size):
        super().__init__(name,price,"Main Course")
        self.serving_size = serving_size

    def apply_discount(self):
        if self.serving_size == "Large":
            return self.price * .10
        else:
            return 0

class Dessert(Food):
    def __init__(self,name, price,sugar_content):
        super().__init__(name, price, "Dessert")
        self.sugar_content = sugar_content

    def apply_discount(self):
        if self.sugar_content >= 30:
            return self.price * .05
        else:
            return 0

class Beverage(Food):
    def __init__(self,name, price, is_alcoholic):
        super().__init__(name, price, "Beverage")
        self.is_alcoholic = is_alcoholic

    def apply_discount(self):
        if self.is_alcoholic:
            return self.price * .12
        else:
            return 0

class Salad(Food):
    def __init__(self, name, price, is_vegetarian):
        super().__init__(name, price, "Salad")
        self.is_vegetarian = is_vegetarian

    def apply_discount(self):
        if self.is_vegetarian:
            return self.price * .15
        else:
            return 0

class Menu:
    def __init__(self):
        self.food = []

    def add_food(self,food):
        self.food.append(food)

    def show_menu(self):
        for food in self.food:
            food.display_details()

menu = Menu()

menu.add_food(Salad("Uyap",6969,True))
menu.add_food(MainCourse("Lechon",500,"Large"))
menu.add_food(Dessert("Tiramisu Cake",100,55))
menu.add_food(Beverage("TooBig",999,True))

print("Menu: ")
menu.show_menu()

#bonus salad
