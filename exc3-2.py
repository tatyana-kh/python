def profile(**kwargs):
    print(f'Ваши данные: {kwargs}')

prof = {}
prof['name'] = input('Введите имя: ')
prof['surname'] = input('Введите фамилию: ')
prof['age'] = int(input('Введите возраст: '))
prof['bdyear'] = int(input('Введите год рождения: '))
prof['city'] = input('Введите город проживания: ')
prof['email'] = input('Введите адрес електронной почты: ')
prof['tel'] = input('Введите номер телефона: ')

profile(**prof)

