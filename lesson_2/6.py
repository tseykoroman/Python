"""
Реализовать структуру данных «Товары». Она должна представлять
собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
"""

choice = ''
my_list = []
my_dict = []
result_dict = dict(название=[], цена=[], количество=[], ед=[])

i = 1
print("\nВведите информацию о товарах.")

while choice != 'q':
    choice = input("\nВведите информацию об отдельном товаре (нажмите любую клавишу для начала ввода) или q для выхода")
    if choice != 'q':
        my_dict = dict({
            'название': str(input("\nВведите название товара")),
            'цена': float(input("\nВведите цену товара")),
            'количество': int(input("\nВведите количество товара")),
            'eд': str(input("\nВведите eдиницу измерения товара"))})
        my_list.append((i, my_dict))
        i += 1
    else:
        for i in range(0, len(my_list)):
            tmp_dict = my_list[i][1]

            names = result_dict.get('название')
            name = str(tmp_dict.get('название'))
            if name not in names:
                names.append(name)

            prices = result_dict.get('цена')
            price = float(tmp_dict.get('цена'))
            if price not in prices:
                prices.append(price)

            amounts = result_dict.get('количество')
            amount = int(tmp_dict.get('количество'))
            if amount not in amounts:
                amounts.append(amount)

            ###units = result_dict.get('eд')
            ###if (str(tmp_dict.get('eд')) not in units):
            ###     units.append(int(tmp_dict.get('eд')))

            result_dict.update({'название': names, 'цена': prices, 'количество': amounts})
            ###result_dict.update({'название': names, 'цена': prices, 'количество': amounts, 'ед': units})
        print(f"Статистика: {result_dict}")
