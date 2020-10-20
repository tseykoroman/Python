"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

try:
    script_name, production, rate, premium = argv
    print("Выработка в часах: ", int(production))
    print("Ставка в час: ", float(rate))
    print("Премия: ", float(premium))
    print(f"Заработная плата сотрудника: {int(production) * float(rate) + float(premium)}")
except (ValueError, ) as err:
    print(err)

