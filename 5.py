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