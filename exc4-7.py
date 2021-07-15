def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def create_generator(n):
    for i in range(1, n):
        yield factorial(i)


for result in create_generator(10):
    print(result)
