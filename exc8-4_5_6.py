class StoreMashines:

    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список - {self.my_store}')

        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'Принтеров на скаладе {self.quantity} шт\n' \
               f'по средней цене {self.price / self.quantity}'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'Сканеров на складе {self.quantity} шт\n' \
               f'по средней цене {self.price / self.quantity}'


class Copier(StoreMashines):
    def to_copier(self):
        return f'Копиров на складе {self.quantity} шт\n' \
               f'по средней цене {self.price / self.quantity}'


unit_1 = Printer('hp', 2000, 5)
unit_2 = Scanner('Canon', 1200, 5)
unit_3 = Copier('Xerox', 1500, 1)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())



