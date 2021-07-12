def int_func(word):
    word = word.title()
    return word

string = input('Введите слова через пробел: ').split()
res = []
for word in string:
    res.append(int_func(word))
print(' '.join(res))
