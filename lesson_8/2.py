'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
'''


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def divide():
        try:
            divider = float(input("Введите делимое: "))
            denominator = float(input("Введите делитель: "))
            if denominator == 0:
                raise OwnError("Деление на 0 запрещено!")
            result = divider / denominator
        except (ValueError, OwnError) as err:
            print(err)
        else:
            print(f"Все хорошо. Результат деления: {result}")


OwnError.divide()
