class Cell:
    def __init__(self, size):
        self.size = int(size)

    def __add__(self, other):
        self.new_size = self.size + other.size
        return f'{self.size} + {other.size} = {self.new_size}'

    def __sub__(self, other):
        self.new_size = self.size - other.size
        return f'{self.size} - {other.size} = {self.new_size}' if self.new_size > 0 \
            else f'{self.size} - {other.size} = клетки больше нет'

    def __mul__(self, other):
        self.new_size = self.size * other.size
        return f'{self.size} * {other.size} = {self.new_size}'

    def __truediv__(self, other):
        self.new_size = round(self.size / other.size)
        return f'{self.size} / {other.size} = {self.new_size}'

    def make_order(self, row):
        result = ''
        for _ in range(int(self.new_size / row)):
            result += '*' * row + '\n'
        result += '*' * (self.new_size % row) + '\n'
        return result


cell_1 = Cell(11)
cell_2 = Cell(11)
print(cell_1 * cell_2)
print(cell_1.make_order(20))
print(cell_1 / cell_2)
print(cell_1.make_order(2))
print(cell_1 - cell_2)
print(cell_1.make_order(3))
print(cell_1 + cell_2)
print(cell_1.make_order(5))
