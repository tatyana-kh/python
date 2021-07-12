def my_sum():
    result = 0
    while True:
        if input('Для выхода из программы нажмите Q, для продолжения Enter ').upper() == 'Q':
            break
        else:
            num = input('введите числа через пробел: ').split()
            for i in num:
                result += int(i)
        print(f'Сумма чисел равна {result}')
    return result

my_sum()




