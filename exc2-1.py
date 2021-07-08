new_list = [25, 'text', 2.36, None, True, (5, 6), [7, 8], {1, 2}]

# до разбора ДЗ было:
# print(new_list)
# for el in new_list:
#    print(type(el))

# исправила
for el, item in enumerate(new_list, 1):
    print(f"{el}) - {item} {type(item)}")
