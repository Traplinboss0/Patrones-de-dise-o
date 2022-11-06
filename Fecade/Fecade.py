class Investor:
    def invest(self):
        print("Investing...")

    def decline(self):
        print("No money!")


class Vendor:
    def give(self):
        print("Giving the materials...")


class Builder:
    def build(self):
        print("Building...")

class Visitor:
    def visit(self):
        print('Visiting')

class BuildingFacade:
    def __init__(self):
        self.investor = Investor()
        self.vendor = Vendor()
        self.builder = Builder()

    def build_project(self):
        for i in range(30):
           self.investor.invest()

        for i in range(40):
            self.vendor.give()

        for i in range(200):
            self.builder.build()




class Fecade:
    def __init__(self):
        self.building_facade = BuildingFacade()
        self.visitor = Visitor()

    def start_project(self):
        self.building_facade.build_project()
        for i in range(100):
            self.visitor.visit()


    print("Project finished!")

if __name__ == '__main__':
    facade = BuildingFacade()
    facade.build_project()


