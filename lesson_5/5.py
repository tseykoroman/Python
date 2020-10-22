"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
try:
    with open('file_5.txt', 'w+') as file_obj:
        line = input('Введите цифры через пробел \n')
        file_obj.writelines(line)
        file_obj.seek(0)
        content = file_obj.read().split(' ')

        print(sum(map(int, content)))
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Неправильно набрана цифра. Ошибка ввода-вывода')
