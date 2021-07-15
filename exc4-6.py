import itertools

start = 10
count_iterator = itertools.count(start=start, step=1)
iterator = itertools.takewhile(lambda x: x <= 100, count_iterator)
for item in iterator:
    print(item)

list = [1, 2, 5, 70, 120]
cycle_iterator = itertools.cycle(list)
iterator = itertools.takewhile(lambda x: x < 50, cycle_iterator)
for item in iterator:
    print(item)
