'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def get_square_coat(self):
        pass

    @abstractmethod
    def get_square_suit(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_coat(self):
        return round(self.width / 6.5 + 0.5)

    def get_square_suit(self):
        return round(self.height * 2 + 0.3)

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани'
                   f' {self.get_square_coat() + self.get_square_suit()}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)

    def __str__(self):
        return f'Площадь на пальто {Clothes.get_square_coat(self)}'


class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)

    def __str__(self):
        return f'Площадь на костюм {Clothes.get_square_suit(self)}'


coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(coat.get_sq_full)
print(suit.get_sq_full)
