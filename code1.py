"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


def not_matrix(matrix):
    i = 1
    while i < len(matrix):  # проверка на одинаковую длину строк внутри матрицы
        if len(matrix[i]) != len(matrix[i - 1]):
            return True
        i += 1
    return False


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):  # малость кривой подход
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print("{:4d}".format(self.matrix[i][j]), end="")
            print()
        return ''

    def __add__(self, other):
        a = not_matrix(self.matrix)
        b = not_matrix(other.matrix)
        if a or b:
            return 'Объект не является матрицей, сложение не возможно\n'
        rez_matrix = []
        if len(self.matrix) == len(other.matrix):  # проверка на кол-во строк
            if len(self.matrix[0]) == len(other.matrix[0]):  # проверка на кол-во столбцов
                for i in range(len(self.matrix)):
                    gen = [(self.matrix[i][j] + other.matrix[i][j]) for j in range(len(self.matrix[i]))]  # генератор
                    rez_matrix.append(gen)
                return Matrix(rez_matrix)
            else:
                return 'Матрицы не равны, сложение не возможно\n'
        else:
            return 'Матрицы не равны, сложение не возможно\n'


obj1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
obj2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
obj3 = Matrix([[1, 4, 5], [2, 3, 4]])
obj4 = Matrix([[1, 2, 3, 4], [1, 1, 2]])

print(obj1)
print(obj2)
print(obj3)
print(obj4)

print(obj1 + obj2)
print(obj1 + obj3)
print(obj1 + obj4)
print(obj2 + obj4)
