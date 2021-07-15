list_a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

list_b = []

removed = []

for elem in list_a:
    if elem in list_b:
        list_b.remove(elem)
        removed.append(elem)
    else:
        list_b.append(elem)

print(list_b)
