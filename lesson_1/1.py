"""Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран."""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

name = "Вася"
print("Меня зовут", name)

number = int(input('Введите целое число от 0 до 100: '))
while number < 100:
    print(number)
    number = number + 1
print('программа завершена успешно')

name = input("Enter your name: ")
print_hi(name)
