def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        result = arg_1 + arg_2
        return result
    elif arg_1 > arg_2 and arg_1 < arg_3:
        result = arg_1 + arg_3
        return result
    else:
        result = arg_2 + arg_3
        return result
arg_1 = int(input("введите первое число: "))
arg_2 = int(input("введите второе число: "))
arg_3 = int(input("введите третье число: "))
print(f'Результат = {my_func(arg_1, arg_2, arg_3)}')
