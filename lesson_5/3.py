"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

try:
    with open("file_3.txt", encoding="utf-8", mode="r") as f_obj:
        sal = []
        small_sal = []
        my_list = f_obj.readlines()
        for i in my_list:
            i = i.split()
            if float(i[1]) < 20000:
                small_sal.append(i[0])
            sal.append(float(i[1]))
    print(f'Оклад меньше 20 000.00 имеют следующие сотрудники: {small_sal}, средняя величина дохода сотрудников: {sum(sal) / len(sal):.2f}')
except IOError:
    print("Произошла ошибка чтения файла!")
except (ValueError, ) as err:
    print(err)
