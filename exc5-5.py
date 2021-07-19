def summ():
    try:
        with open('new_exc5-5.txt', 'w+') as file:
            line = input('Введите цифры через пробел - ')
            file.writelines(line)
            num = line.split()

            print(sum(map(int, num)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода')
summ()
