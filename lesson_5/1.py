"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

try:
    with open("file_1.txt", encoding="utf-16", mode="w") as f_obj:
        while True:
            line = input('Введите текст \n')
            f_obj.writelines(line+'\n')
            if not line:
                break
except IOError:
    print("Произошла ошибка ввода-вывода!")
