
new_list = [7, 6, 6, 5, 4, 3, 3, 2]
new_num = int(input("Введите натуральное число: "))

i = 0
for el in new_list:
    if new_num <= el:
        i += 1
new_list.insert(i, new_num)
print(new_list)
