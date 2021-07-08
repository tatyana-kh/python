# до разбора ДЗ
new_str = input('введите несколько слов через пробел: ')
new_str = new_str.split()
for num, el in enumerate(new_str):
    print(num, el[:10])

