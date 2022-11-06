from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer):

        pass

    @abstractmethod
    def detach(self, observer: Observer):

        pass

    @abstractmethod
    def notify(self):

        pass


class ConcreteSubject(Subject):

    _observers: List[Observer] = []


    def attach(self, observer: Observer):
        print("Asunto: Adjunto un observador.")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):


        print("Asunto: Notificación a los observadores ...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):


        print("\nAsunto: Estoy haciendo algo importante.")
        self._state = randrange(0, 10)

        print(f"Asunto: Mi estado acaba de cambiar a: {self._state}")
        self.notify()


class Observer(ABC):


    @abstractmethod
    def update(self, subject: Subject):

        pass




class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        if subject._state < 3:
            print("ObservadorA: reaccionó al evento")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        if subject._state == 0 or subject._state >= 2:
            print("ObservadorB: reaccionó al evento")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()