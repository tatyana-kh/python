list_a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_b = [el for i, el in enumerate(list_a) if i > 0 and list_a[i] > list_a[i - 1]]

print(list_b)
