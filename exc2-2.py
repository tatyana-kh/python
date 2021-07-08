# первый вариант до разбора ДЗ
a = input('Введите список значений через пробел: ')
new_list = a.split()
print(new_list)

i = 0
while i < len(new_list) - 1:
    el = new_list[i]
    el2 = new_list[i + 1]
    new_list[i] = el2
    new_list[i + 1] = el
    i += 2

print(new_list)

# второй вариант до разбора ДЗ

a = input('Введите список значений через пробел: ')
new_list = a.split()
print(new_list)

i = 0
while i < len(new_list) - 1:
    new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
    i += 2

print(new_list)
