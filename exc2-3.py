# первый вариант до разбора ДЗ
seasons = ['зима', 'весна', 'лето', 'осень']

month = input('введите номер месяца: ')

if month.isdigit():
    month = int(month)
    if month == 1 or month == 2 or month == 12:
        print(seasons[0])
    elif month == 3 or month == 4 or month == 5:
        print(seasons[1])
    elif month == 6 or month == 7 or month == 8:
        print(seasons[2])
    elif month == 9 or month == 10 or month == 11:
        print(seasons[3])
    else:
        print('введено неверное число')

else:
    print('это не номер')

# второй вариант до разбора ДЗ
seasons = {1: 'зима', 2: 'зима', 12: 'зима',
           3: 'весна', 4: 'весна', 5: 'весна',
           6: 'лето', 7: 'лето', 8: 'лето',
           9: 'осень', 10: 'осень', 11: 'осень'
           }

month = input('введите номер месяца: ')
if month.isdigit():
    month = int(month)
    if month > 0 and month <= 12:
        print(seasons.get(month))
    else:
        print('введено неверное число')
else:
    print('это не номер')
