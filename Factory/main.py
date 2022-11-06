from factory import FactoryCar

def main():
    auto1 = FactoryCar.get_car("Deportivo", "Toyota")
    auto2 = FactoryCar.get_car("Familiar", "Suzuki")
    auto1.nitro()
    auto2.nitro()

main()
