from abc import ABC, abstractmethod


class ICalc(ABC):

    @abstractmethod
    def calculate(self):
        pass


class IMicrowave(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass