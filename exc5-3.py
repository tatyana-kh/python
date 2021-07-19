with open('exc5-3.txt', 'r') as f:
    workers = {}
    num = 0
    for line in f:
        key, value = line.split()
        workers[key] = value
        num += 1
        if int(value) < 20000:
            print(f'Оклад менее 20 тыс.: {key}')
    sum1 = sum(float(x) for x in workers.values())
    sev = sum1/num
    print(f'Средняя зарплата сотрудников = {sev}')

