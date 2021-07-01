rev = float(input('Введите доходы: '))
exp = float(input('Введите расходы: '))
profit = rev - exp
if rev > exp:
    print('Прибыль составила:', "%.2f" % (profit))
    print('Рентабельность:', "%.2f" % (profit / rev))
    emp = int(input('Введите количество сотрудников: '))
    print('Прибыль на каждого сотрудника составила:', "%.2f" % (profit / emp))
elif exp == rev:
    print('Прибыль отсутствует.')
else:
    print('Убыток составил:', "%.2f" % (exp - rev))


