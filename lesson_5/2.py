"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open("file_2.txt", encoding="utf-8", mode="r") as f_obj:
        content = f_obj.readlines()
        print(f'Содержимое файла: \n {f_obj.read()}')
        print(f'Количество строк в файле - {len(content)}')
        for i in range(len(content)):
            print(f'Количество слов в {i + 1} - ой строке: {len(content[i].split())}')
except IOError:
    print("Произошла ошибка чтения файла!")
