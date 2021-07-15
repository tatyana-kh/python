def salary_calc():
    time = float(input('Введите количество отработанных часов: '))
    sal = float(input('Введите часовую ставку: '))
    bonus = float(input('Введите размер премии: '))
    salary = time * sal
    return salary + bonus

print(f'Размер заработной платы составил: {salary_calc()}')
