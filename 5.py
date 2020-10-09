"""Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""
proceeds = float(input("Введите выручку - "))
costs = float(input("Введите издержки - "))
if proceeds > costs:
    print('Фирма работает с прибылью')
    print("Рентабельность выручки {:.2f}".format((proceeds - costs)/proceeds))
    employees = int(input("Введите численность сотрудников - "))
    print("Прибыль фирмы в расчете на одного сотрудника {:.2f}".format((proceeds - costs) / employees))
# Иначе, т.е. если неправильный пароль
else:
    print('Фирма работает с убытком')
