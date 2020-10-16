"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
"""
def user_info(name, surName, birthYear, birthCity, email, phone):
    """Выводит в консоль данные пользователя.

    Именованные параметры:
    name -- имя
    surName -- фамилия
    birthYear -- год рождения
    birthCity -- город проживания
    email -- e-mail
    phone -- телефон
    """
    print(f"Имя - {name}; фамилия - {surName}; год рождения - {birthYear}; город проживания - {birthCity}; email - {email}; телефон - {phone}")

def user_info_second(**kwargs):
    """Выводит в консоль данные пользователя.

    Именованные параметры:
    name -- имя
    surName -- фамилия
    birthYear -- год рождения
    birthCity -- город проживания
    email -- e-mail
    phone -- телефон
    """
    print(f"Имя - {kwargs.get('name')}; фамилия - {kwargs.get('surName')}; год рождения - {kwargs.get('birthYear')}; город проживания - {kwargs.get('birthCity')}; email - {kwargs.get('email')}; телефон - {kwargs.get('phone')}")

try:
    name = str(input("Укажите имя: "))
    surName = str(input("Укажите фамилию: "))
    birthYear = int(input("Укажите год рождения: "))
    birthCity = str(input("Укажите город проживания: "))
    email = str(input("Укажите e-mail: "))
    phone = str(input("Укажите телефон: "))
except (ValueError, ) as err:
    print(err)

user_info(name=name, surName=surName, birthYear=birthYear, birthCity=birthCity, email=email, phone=phone)
user_info_second(name=name, surName=surName, birthYear=birthYear, birthCity=birthCity, email=email, phone=phone)
