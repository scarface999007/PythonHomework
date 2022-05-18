from homework_7_module.Cell import Cell
from homework_7_module.Matrix import Matrix
from homework_7_module.task_num_2.Clothes import Clothes

# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод__init__()),
#    который должен принимать данные (список списков) для формирования матрицы.
#    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
#    Matrix (двух матриц). Результатом сложения должна быть новая матрица.

lists = [[1, 4, 5, 12],
         [-5, 8, 9, 0],
         [-6, 7, 11, 19]]

other_lists = [[1, -4, -5, -12],
               [5, -8, -9, 0],
               [6, -7, -11, 19]]

matrix = Matrix(lists)
other_matrix = Matrix(other_lists)
print(matrix)
print(other_matrix)
print(matrix + other_matrix)

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.

clothes = Clothes("Title1")
clothes.add_coat(65)
clothes.add_suit(20)
print(clothes.fabric_consumption)

# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.

cell1 = Cell(12)
cell2 = Cell(12)

print((cell1 + cell2).element)
print((cell1 - cell2).element)
print((cell1 * cell2).element)
print((cell1 / cell2).element)

print(cell1.make_order(5))
