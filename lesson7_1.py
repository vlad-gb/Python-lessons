#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 1")


class Matrix:
    """ A simple Python matrix class with
    operator overloading +"""

    def __init__(self, matrix):
        self.rows = matrix
        self.m = len(self.rows[0])  # columns number
        self.n = len(self.rows)  # rows number

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return '\n' + s + '\n'

    def get_rank(self):
        return self.m, self.n

    def __add__(self, mat):
        """ Add a matrix to this matrix and
        return the new matrix. Doesn't modify
        the current matrix """

        if self.get_rank() != mat.get_rank():
            Exception("Trying to add matrices of varying rank!")

        ret = [None for row in range(self.n)]

        print(f"Ret is {len(ret)}")

        for x in range(self.m):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        res_mat = Matrix(ret)

        return res_mat


list1_3x3 = [[3, 5, 32],
             [2, 4, 6],
             [-1, 64, -8]
             ]

matrix1_3x3 = Matrix(list1_3x3)
print(f"Matrix1 is: {matrix1_3x3}")

list2_3x3 = [[1, 1, 1],
             [0, 0, 0],
             [-1, -1, -1]
             ]

matrix2_3x3 = Matrix(list2_3x3)
print(f"Matrix2 is: {matrix2_3x3}")

sum_matrix_1_and_2 = matrix1_3x3 + matrix2_3x3
print(f"Sum of matrices 1 and 2 is: {sum_matrix_1_and_2}")

print("It's all done")
