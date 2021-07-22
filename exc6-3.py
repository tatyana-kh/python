class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus};

class Position(Worker):
    def get_full_name(self): # методы получения полного имени сотрудника
        return self.name + ' ' + self.surname

    def get_total_income(self): # дохода с учётом премии
        return float(self._income["wage"]) + float(self._income["bonus"])
        # return sum(self._income.values())

profile = Position('Ivan', 'Ivanov', 'engineer', '70000', '10000')
print(f'Полное имя сотрудника: {profile.get_full_name()}\n'
      f'Доход с учетом премии: {profile.get_total_income()}')

