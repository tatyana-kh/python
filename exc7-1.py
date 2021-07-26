class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f'{i:2}', end='')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)


my_list_1 = Matrix([[5, 3, 1, 0], [2, 0, 4, 7], [6, -1, 0, 3], [2, 3, 4, 5]])
my_list_2 = Matrix([[-5, 3, 4], [-2, 0, -4], [4, 6, 8], [3, 0, -3]])
print(my_list_1.__add__(my_list_2))

