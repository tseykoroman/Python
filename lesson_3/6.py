"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()
"""


def my_func():
    """Принимает набор слов из маленьких латинских букв и возвращает их же, но с прописной первой буквой.
    Слова, содержащие не только латинские буквы, - игнорируются."""
    my_list = [item for item in input("Введите предложение, состоящее из слов на латинице: ").split()]
    result = ""
    for el in my_list:
        for letter in list(el):
            if not (97 <= ord(letter) <= 122 or ord(letter) >= 65 and ord(letter) <= 90):
                el = None
        if el is not None:
            if len(result) > 0:
                result = result + " " + str(el).title()
            else:
                result = el.capitalize()
    print(f"{result}")


my_func()
