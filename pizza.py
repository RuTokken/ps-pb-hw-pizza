class Product:
    def __init__(self, title, calorific, cost):
        if Product.check_title(title) and Product.check_calorific(calorific) and Product.check_cost(cost): 
            self.title = title
            self.__calorific = calorific
            self.__cost = cost
        else:
            raise ValueError

    staticmethod
    def check_title(title):
        if title:
            return True
        else:
            return False

    @staticmethod
    def check_calorific(calorific):
        return calorific > 0

    @property
    def calorific(self):
        return self.__calorific
    
    @calorific.setter
    def calorific(self, calorific):
        if Product.check_calorific(calorific):
            self.__calorific = calorific
        else:
            raise ValueError  

    @staticmethod
    def check_cost(cost):
        return cost > 0

    @property
    def cost(self):
        return self.__cost
    
    @cost.setter
    def cost(self, cost):
        if Product.check_cost(cost):
            self.__cost = cost
        else:
            raise ValueError

class Ingredient:
    def __init__(self, product, weight):
        if Ingredient.check_weight(weight):
            self.product = product
            self.__weight = weight
        else:
            raise ValueError

    @staticmethod
    def check_weight(weight):
        return weight > 0

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        if Ingredient.check_weight(weight):
            self.__weight = weight
        else:
            raise ValueError

    def get_kkal(self):
        kkal = self.weight / 100 * self.product.calorific
        return kkal

    def get_price(self):
        price = self.weight / 100 * self.product.cost
        return price

class Pizza(Ingredient):
    def __init__(self, title, ingredients):
        if Pizza.check_title(title):
            self.title = title
            self.ingredients = ingredients

    @staticmethod
    def check_title(title):
        if title:
            return True
        else:
            return False


Cheese = Product('Сыр', 57, 63)
Chicken = Product('Курица', 120, 40)
Pineapple = Product('Ананас', 90, 32)
Sauce = Product('Соус', 8, 6)
Dough = Product('Тесто', 65, 45)
Champignons = Product('Шампиньоны', 45, 23)

In1 = Ingredient(Cheese, 150)
In2 = Ingredient(Chicken, 200)
In3 = Ingredient(Pineapple, 30)
In4 = Ingredient(Sauce, 20)
In5 = Ingredient(Dough, 300)
In6 = Ingredient(Champignons, 198)

Festive = Pizza('Праздничная', [In1, In2, In3, In4, In5, In6])

total_kkal = 0
total_price = 0
for i in range (0, len(Festive.ingredients)):
    total_kkal += Festive.ingredients[i].get_kkal()
    total_price += Festive.ingredients[i].get_price()

print(f'{Festive.title} ({total_kkal} kkal) - {total_price} руб')