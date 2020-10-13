"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

my_list = [7, 5, 3, 3, 2]
print(my_list)
choice = ''

while choice != 'q':
    choice = input("\nВведите следующее значение или q для выхода")
    if choice != 'q':
        for el in range(len(my_list)):
            if my_list[el] == int(choice):
                my_list.insert(el + 1, int(choice))
                break
            elif my_list[0] < int(choice):
                my_list.insert(0, int(choice))
                break
            elif my_list[-1] > int(choice):
                my_list.append(int(choice))
                break
            elif my_list[el] > int(choice) > my_list[el + 1]:
                my_list.insert(el + 1, int(choice))
                break
        print(my_list)
