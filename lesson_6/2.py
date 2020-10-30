'''Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании
экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной
в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def square(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, mass, thickness):
        super().__init__(_length, _width)
        self._mass = mass
        self._thickness = thickness

    def mass(self):
        return print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна в тоннах - {super().square() * self._mass * self._thickness / 1000}')


r = MassCount(20, 5000, 25, 5)
r.mass()
