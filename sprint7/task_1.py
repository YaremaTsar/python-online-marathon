'''
You have to create a main course and a dessert at an Italian and a French restaurant, but you won't mix one cuisine with
 the other.

Your task is:

1) define a class Product with an abstract method cook(). This class would be base class for the next classes:

- class FettuccineAlfredo with field name ("Fettuccine Alfredo"), method cook() provides an output of the formatted string
 "Italian main course prepared: " and name of the dish;

 - class Tiramisu, with field name ("Tiramisu"), method cook() provides an output of the formatted string "Italian dessert
 prepared:" and name of the dish;

- class DuckALOrange, with field name ("Duck À L'Orange"), method cook() provides an output of the formatted string "French
main course prepared: " and name of the dish;

- class CremeBrulee,  with field name ("Crème brûlée"), method cook() provides an output of the formatted string "French
dessert prepared: " and name of the dish.

2) define a class Factory with an abstract method get_dish() that takes  type_of_meal as a parameter. This class would be
base class for the classes ItalianDishesFactory and FrenchDishesFactory. The method get_dish() according to type_of_meal
("main" or "dessert") invokes the dish of appropriate cousine;

3) define a class FactoryProducer with the method get_factory(). The method takes the parameter type_of_factory and invokes
the appropriate dishes factory (classes ItalianDishesFactory or FrenchDishesFactory).
'''

from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    field_name = "Fettuccine Alfredo"

    def cook(cls):
        print(f"Italian main course prepared: {cls.field_name}")


class Tiramisu(Product):
    field_name = "Tiramisu"

    def cook(cls):
        print(f"Italian dessert prepared: {cls.field_name}")


class DuckALOrange(Product):
    dish = "Duck À L'Orange"

    def cook(cls):
        print(f"French main course prepared: {cls.dish}")


class CremeBrulee(Product):
    dish = "Crème brûlée"

    def cook(cls):
        print(f"French dessert prepared: {cls.dish}")


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def get_dish(cls, type_of_meal: str):
        pass


class ItalianDishesFactory(Factory):
    def get_dish(cls, type_of_meal: str):
        if type_of_meal == "main":
            return FettuccineAlfredo()
        elif type_of_meal == "dessert":
            return Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(cls, type_of_meal: str):
        if type_of_meal == "main":
            return DuckALOrange()
        elif type_of_meal == "dessert":
            return CremeBrulee()


class FactoryProducer:

    def get_factory(self, type_of_factory: Factory):
        if type_of_factory == "italian":
            return ItalianDishesFactory()
        elif type_of_factory == "french":
            return FrenchDishesFactory()
