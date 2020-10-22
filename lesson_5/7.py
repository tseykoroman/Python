"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

companies_dict = {}
average_profit_dict = {}
sum_profit = 0
profit_count = 0
with open("file_7.txt", encoding="utf-8", mode="r") as file_obj:
    avg_profit = 0
    for line in file_obj:
        items = line.split()
        profit = float(items[2]) - float(items[3])
        companies_dict[items[0]] = profit
        if profit > 0:
            sum_profit += profit
            profit_count += 1
    average_profit_dict["average_profit"] = sum_profit / profit_count
    print(f'Фирмы и их прибыли - \n{companies_dict}')
    print(f'Средняя прибыль - \n{average_profit_dict}')
with open("file_7.json", encoding="utf-16", mode="w") as write_f:
    json.dump([companies_dict, average_profit_dict], write_f, ensure_ascii=False, indent=4, separators=(',', ': '))
