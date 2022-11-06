class car:
    def __init__(self, brand):
        self.brand = brand
        self.estate = 0

    def arranca(self):
        if self.__estate == 0:
            print('arrancando el atomovil', self.brand)
            self.__estate = 1
        else:
            print('el auto', self.brand, 'no se ha detenido')

    def detener(self):
        if self.__estate == 1:
            print('Deteniendo el auto', self.brand)
            self.__estate = 0
        else:
            print('El auto', self.brand, 'no ha arrancado')

    def nitro(self):
        print ('aplicando nitro al auto')

class SportCar(car):

    def __init__(self, brand):
        super(SportCar, self).__init__(brand)
        print('Tienes un car deportivo brand', self.brand)

class FamilyCar(car):

    def __init__(self, brand):
        super(FamilyCar, self).__init__(brand)
        print("Tienes un car familiar brand", self.brand)

    def nitro(self):
        print("El auto familiar no tiene nitro")
