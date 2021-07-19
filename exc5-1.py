with open('exc5-1.txt','w') as f:
    while True:
        s = input('Введите данные: ')
        if s == '': break
        f.write(s+'\n')

f = open('exc5-1.txt','r')
print(f.read())
f.close()
