# lab №2 ex. 3 | Var 4 Sergey Zubrilin 10/15/18


import numpy as np
from lab_2.ex1 import MatrixTool


class MatrixTollEx3(MatrixTool):
    def __init__(self):
        MatrixTool.__init__(self)
        self.matrix_ex3_1 = []
        self.matrix_ex3_2 = []

    def build_matrix(self):
        """
        Генерирует тестовые матрицы
        """
        self.matrix_ex3_1 = np.array([[7, 6, 5, 6, 8], [6, 7, 0, 4, 3], [-2, 7, 6, -3, -1],
                                     [2, 0, 5, 4, 7], [8, -2, 3, 1, 3]])
        self.matrix_ex3_2 = np.array([[-3, 8, 9, -2, 0], [3, -5, 2, -5, 5], [3, 7, 2, 7, 3],
                                      [-3, 4, 7, -4, 6], [9, 9, 3, -3, 6]])

    @staticmethod
    def is_positively_defined(matrix):
        """
        Метод, проверяющуй по критерию Сильвестра, является ли
        матрица положительно определённой.
        :return bool
        """
        for _ in range(len(matrix) - 1):
            if np.linalg.det(matrix[:-1, :-1]) < 0:
                return False
            matrix = matrix[:-1, :-1]
        return True


def test_ex3():
    ex3 = MatrixTollEx3()
    print('Искомые матрицы для проверки')
    print('---------------------------------------------------------------')
    ex3.build_matrix()
    print(ex3.matrix_ex3_1, end='\n')
    print('---------------------------------------------------------------')
    print(ex3.matrix_ex3_2)
    print('---------------------------------------------------------------')
    print('Проверка по критерию Сильвестра  ')
    print('---------------------------------------------------------------')
    print(f'Первая тестовая матрица. Положительно определенная -> {ex3.is_positively_defined(ex3.matrix_ex3_1)}')
    print(f'Вторая тестовая матрица. Положительно определенная -> {ex3.is_positively_defined(ex3.matrix_ex3_2)}')


test_ex3()
