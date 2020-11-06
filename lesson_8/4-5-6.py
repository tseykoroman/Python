'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''

from abc import ABC, abstractmethod
from copy import deepcopy


class Storage(ABC):
    storage = []
    bookkeeping = []
    hr = []
    marketers = []
    department = 0

    @abstractmethod
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def addToStorageManual(self):
        try:
            code = input(f'Введите код ')
            brand = (input(f'Введите фирму '))
            quantity = int(input(f'Введите количество '))
            unique = {'code': code, 'brand': brand, 'quantity': quantity}
            self.storage.append(unique)
            print('Товар с характеристиками фирма -', brand, ', количество - ',
                  quantity, ', отправлен на склад')
        except (ValueError) as err:
            print(err)

    def sendToStorage(self):
        self.storage.append(self.kwargs)
        print(self.__class__.__name__, self.kwargs['code'], ', фирма -', self.kwargs['brand'], ', количество - ', self.kwargs['quantity'], ', отправлен на склад')

    def showContent(self, x):
        print('----------------------------------------\n')
        if x == 'основной склад':
            self.department = self.storage
        elif x == 'бухгалтерия':
            self.department = self.bookkeeping
        elif x == 'отдел кадров':
            self.department = self.hr
        elif x == 'маркетологи':
            self.department = self.marketers
        else:
            return print('Такого подразделения пока не существует')
        if self.department is not False:
            print(f'В подразделении "{x}" имеются следующие элементы: ')
            for i in self.department:
                if i['quantity'] == 0:
                    del i
                else:
                    print(i['code'], i['brand'], i['quantity'], 'шт')
            j = 0
            for _ in self.department:
                j += _['quantity']
            print('В данный момент в подразделении', j, 'товаров')

    def sendToDepartment(self, code, quantity, departmentName):
        print('----------------------------------------\n')
        self.department = 0
        try:
            for i in deepcopy(self.storage):
                if code == i['code']:
                    if i['quantity'] < quantity:
                        print('Нельзя отправить больше товара чем мы имеем!')
                        return
                    else:
                        if departmentName == "бухгалтерия":
                            self.department = self.bookkeeping
                        elif departmentName == "отдел кадров":
                            self.department = self.hr
                        elif departmentName == "маркетологи":
                            self.department = self.marketers
                        else:
                            print(f'Отдела "{departmentName}" не существует')
                            return
                        self.department.append(i)
                        self.department[-1]['quantity'] = quantity
                        print(f'Товар c артикулом {code} перемещен в подразделение "{departmentName}"')
            if self.department == 0:
                print('Товара с таким артикулом не существует!!!')
            else:
                for i in self.storage:
                    if code == i['code']:
                        i['quantity'] -= quantity
                    if int(i['quantity']) <= 0:
                        del i
        except TypeError:
            print('Введены некорректные данные!!! Артикул и количество товара передаются в виде цифр')


class OfficeEquipment(Storage):
    def __init__(self, **kwargs):
        super().__init__()
        self.kwargs = kwargs


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = self.__class__.__name__
        self.kwargs = kwargs


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = self.__class__.__name__
        self.kwargs = kwargs


class Copier(Scanner, Printer):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = self.__class__.__name__
        self.kwargs = kwargs


a_1 = Copier(code=45446,
             brand='Xerox',
             color='Black',
             price=4654,
             quantity=10,
             format_='A4',
             scanning_technology='CIS',
             print_type='Color',
             print_speed=15,
             printing_technology='jet')
a_2 = Scanner(code=123132,
              brand='HP',
              color='white',
              price=13212,
              quantity=10,
              format_='A4',
              scanning_technology='CIS')
a_3 = Printer(code=654658,
              brand='brother',
              color='Black',
              price=65468,
              quantity=10,
              print_type='Black',
              print_speed=8,
              printing_technology='laser')

storage = OfficeEquipment()
a_1.sendToStorage()
a_2.sendToStorage()
a_3.sendToStorage()
print()
print(
    'Помимо основного склада, на данный момент есть три подразделения - бухгалтерия, отдел кадров и маркетологи. '
    '\nЭти подразделения можно передавать в качестве параметров для передачи товаров на них.'
    '\nПервым параметром идет артикул товара, вторым количество товара, третим на какой склад отправить товар')
storage.showContent('основной склад')
storage.showContent('бухгалтерия')
storage.sendToDepartment(45446, 10, 'бухгалтерия')
storage.sendToDepartment(123132, 10, 'отдел кадров')
storage.sendToDepartment(654658, 10, 'маркетологи')
storage.sendToDepartment(45446, 3, 'АХО')
storage.showContent('отдел кадров')
storage.showContent('бухгалтерия')
storage.showContent('маркетологи')
storage.showContent('основной склад')
storage.addToStorageManual()

