from car import SportCar,FamilyCar

class FactoryCar:

    @staticmethod
    def get_car(tipo, brand):
        if tipo == "Deportivo":
            return SportCar(brand)
        elif tipo == "Familiar":
            return FamilyCar(brand)
        else:
            return "Tipo invalido"