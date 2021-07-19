dict = {}
with open('exc5-6.txt', 'r') as f:
    for line in f:
        sub, lec, pract, lab = line.split()
        dict[sub] = int(lec) + int(pract) + int(lab)
    print(f'Итого часов по предмету - {dict}')

