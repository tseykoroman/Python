"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

try:
    digits_dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять'
    }
    with open("file_4.txt", encoding="utf-8", mode="r") as f_obj:
        with open("file_4_new.txt", encoding="utf-16", mode="w") as file_obj_2:
            for line in f_obj:
                eng_digit = line.split(' ', 1)
                file_obj_2.write(digits_dict[eng_digit[0]] + ' ' + eng_digit[1])
except IOError:
    print("Произошла ошибка ввода-вывода!")
