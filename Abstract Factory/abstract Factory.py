from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def cook(self):
        pass


class Empanadas(Product):
    name = "Empanadas"

    def cook(self):
        print("plato argento: " + self.name)


class Chocotorta(Product):
    name = "Chocotorta"

    def cook(self):
        print("Postre argento: " + self.name)


class Pizza(Product):
    name = "Pizza"

    def cook(self):
        print("Plato Italiano: " + self.name)


class Tiramisu(Product):
    name = "Tiramisu"

    def cook(self):
        print("Postre Italiano: " + self.name)


class Factory(ABC):  # Fabrica Abstracta

    @abstractmethod
    def get_dish(type_of_meal):
        pass


class Argento_Factory(Factory):  # Fabrica Concreta

    def get_dish (type_of_meal):
        if type_of_meal == "Principal":
            return Empanadas()
        if type_of_meal == "Postre":
            return Chocotorta()


class Italian_Factory(Factory):  # Fabrica Concreta

    def get_dish(type_of_meal):
        if type_of_meal == "Principal":
            return Pizza()

        if type_of_meal == "Postre":
            return Tiramisu()


class FactoryProducer:

    def get_factory(self, type_of_factory):
        if type_of_factory == "Argento":
            return Argento_Factory
        if type_of_factory == "Italiana":
            return Italian_factory


print("\n")

fp = FactoryProducer()

fac = fp.get_factory("Argento")
main = fac.get_dish("principal")
main.cook()
dessert = fac.get_dish("postre")
dessert.cook()



