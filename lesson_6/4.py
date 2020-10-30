'''
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} стартует'

    def stop(self):
        return f'{self.name} останавливается'

    def turn_right(self):
        return f'{self.name} поворачивает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Указанная скорость {self.speed} для {self.name} выше, чем позволено для городской машины'
        else:
            return(f'Текущая скорость городской машины {self.name} равна {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Указанная скорость {self.speed} для {self.name} выше, чем позволено для рабочей машины'
        else:
            print(f'Текущая скорость рабочей машины {self.name} равна {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - принадлежит отделу ГИБДД'
        else:
            return f'{self.name} - не принадлежит отделу ГИБДД'


mazda = SportCar(100, 'Оранжевая', 'Мазда', False)
oka = TownCar(30, 'Желтая', 'Ока', False)
opel = WorkCar(70, 'Черный', 'Опель', True)
kia = PoliceCar(110, 'Розовый', 'Киа', True)
print(opel.turn_left())
print(f'Если {oka.turn_right()}, то {mazda.stop()}')
print(f'{oka.go()}')
print(f'{oka.show_speed()}')
print(f'{opel.show_speed()}')
print(f'{opel.name} - {opel.color}')
print(f'Принадлежит ли {mazda.name} отделу ГИБДД? {mazda.is_police}')
print(f'Принадлежит ли {opel.name} отделу ГИБДД? {opel.is_police}')
print(mazda.show_speed())
print(oka.show_speed())
print(kia.police())
print(kia.show_speed())
