def my_div():
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    while num_2 == 0:
        print('Деление на ноль запрещено')
        num_2 = int(input('Введите второе число: '))
    result = num_1 / num_2
    return result

print(f'Частное чисел = {my_div()}')
