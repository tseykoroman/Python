"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""
my_list = [2, 'text', 456, 45.3, None, (4, 234, 45.8, "text", "word", "el", True, None)]
for i in my_list:
        print(f"Тип переменной: {type(i)}, значение: {i}")
