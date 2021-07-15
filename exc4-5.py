from functools import reduce

list = [el*2 for el in range(50, 501)]
print(list)
result = reduce((lambda x, y: x * y), list)
print(result)
