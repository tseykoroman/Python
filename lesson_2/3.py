"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn'}
month = int(input("Введите номер месяца "))
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(0))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(1))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(2))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(3))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")

################################################################

def get_season_index(month):
    return {
        month == 1 or month == 2 or month == 12: 0,
        month == 3 or month == 4 or month == 5: 1,
        month == 6 or month == 7 or month == 8: 2,
        month == 9 or month == 10 or month == 11: 3
    }[True]

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn'}
month = int(input("Введите номер месяца - от 1 до 12"))
print(seasons_dict.get(get_season_index(month)))
print(seasons_list[get_season_index(month)])
