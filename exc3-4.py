def my_func(x, y):
    res = x ** abs(y)
    return res

x = int(input("введите число: "))
y = int(input("введите степень числа: "))
print(my_func(x, y))

# второй вариант не получился