from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, name, param):
        self.name = name
        self.param = param

    @abstractmethod
    def tissue_cons(self):
        pass

    @property
    def sum(self, result):
        self.result = self.param / 6.5 + 0.5 + 2 * self.param + 0.3
        return f'Сумма затраченной ткани равна: {result :.2f}'

class Coat(Clothes):
    def tissue_cons(self):
        return f'Расход ткани для пошива {self.name}: {self.param / 6.5 + 0.5 :.2f} метров'


class Costume(Clothes):
    def tissue_cons(self):
        return f'Расход ткани для пошива {self.name}: {2 * self.param + 0.3 :.2f} метров'


coat = Coat('Пальто', 56)
costume = Costume('Костюм', 170)
print(Clothes.sum)
print(costume.tissue_cons())
print(coat.tissue_cons())


