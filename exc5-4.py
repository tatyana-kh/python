rep = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('exc5-4.txt', 'r') as f1:
    for i in f1:
        i = i.split(' ', 1)
        new_file.append(rep[i[0]] + '  ' + i[1])
    print(new_file)

with open('new_exc5-4.txt', 'w') as f2:
    f2.writelines(new_file)
