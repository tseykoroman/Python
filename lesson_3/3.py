"""
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    """Возвращает сумму наибольших двух аргументов.
    (number, number, number) -> number

    >>> my_func(1.0, 2.0, 3.0)
    5.0
    """
    if len(args) > 3:
        print("Максимальное количество аргументов в функции - 3.")
    result_tuple = [x for x in args if x != min(args)]
    if len(result_tuple) == 0:
        print(float(args[0] + args[1]))
    else:
        print(sum(result_tuple))


try:
    first_param = float(input("Укажите первый аргумент: "))
    second_param = float(input("Укажите второй аргумент: "))
    third_param = float(input("Укажите третий аргумент: "))
except (ValueError,) as err:
    print(err)

my_func(first_param, second_param, third_param)
