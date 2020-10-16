"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
"""


def my_func(my_list):
    """Возвращает сумму чисел.
    (number, number, number, ...) -> number

    >>> my_func(1.0, 2.0, 3.0)
    6.0

    """
    sum = 0
    for el in my_list:
        try:
            sum += float(el)
        except ValueError:
            continue
    return sum


result = 0
while True:
    my_list = [item for item in input("Введите слагаемые через пробел (q для выхода): ").split()]
    if 'q' in my_list:
        result += my_func(my_list)
        print(f"{result}")
        break
    local_sum = my_func(my_list)
    result += local_sum
    print(f"{local_sum}({result})")
