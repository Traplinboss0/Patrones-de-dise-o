from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    def __init__(self, strategy: Strategy):


        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:


        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_business_logic(self):

        print("ordena datos usando la estrategia ")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":


    context = Context(ConcreteStrategyA())
    print("Cliente: la estrategia está establecida en la clasificación normal.")
    context.do_some_business_logic()
    print()

    print("Cliente: la estrategia está configurada para invertir la clasificación.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()