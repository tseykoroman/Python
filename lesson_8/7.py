'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        if b > 0:
            return f'z = {a} + {b} * i'
        else:
            return f'z = {a} {b} * i'

    def __mul__(self, other):
        a = self.a * other.a - (self.b * other.b)
        b = self.a * other.b + self.b * other.a
        if b > 0:
            return f'z = {a} + {b} * i'
        else:
            return f'z = {a} {b} * i'

    def __str__(self):
        if self.b > 0:
            return f'z = {self.a} + {self.b} * i'
        else:
            return f'z = {self.a} {self.b} * i'



z_1 = ComplexNumber(2, 3)
z_2 = ComplexNumber(-1, 1)
z_3 = ComplexNumber(5, -6)
z_4 = ComplexNumber(-3, 2)
print(f'Первое комплексное число - {z_1} \n ')
print(f'Второе комплексное число - {z_2} \n ')
print(f'Третье комплексное число - {z_3} \n ')
print(f'Четвертое комплексное число - {z_4} \n ')

print(f'Сумма первых двух комплексных чисел - {z_1 + z_2} \n ')
print(f'Произведение первых двух комплексных чисел - {z_1 * z_2} \n ')
print(f'Сумма вторых двух комплексных чисел - {z_3 + z_4} \n ')
print(f'Произведение вторых двух комплексных чисел - {z_3 * z_4} \n ')
