# lab №2 ex. 2 | Var 4 Sergey Zubrilin 10/14/18


import numpy as np
from lab_2.ex1 import MatrixTool


class MatrixTollEx2(MatrixTool):
    def build_matrix(self):
        """
        Cконструировать блочную матрицу (используя функции для заполнения
        стандартных матриц)
        """
        self.matrix = np.vstack([np.hstack([np.ones((3, 3), dtype=int), np.full_like(np.empty((3, 3), dtype=int), -1)]),
                                 np.hstack([np.full_like(np.empty((3, 3), dtype=int), 2), np.eye(3, dtype=int)*3])],)

    def task_for_ex2(self):
        """
        'применить функции обработки данных и поэлементные
        операции для нахождения заданных величин.'
        :return: int
        """
        return np.sum(self.matrix.diagonal()[:6]**3)


def test_ex2():
    ex2 = MatrixTollEx2()
    ex2.build_matrix()
    print('Искходная матрицы ->')
    print(ex2.matrix, end='\n\n')
    print('Заданная величина ->')
    print(ex2.task_for_ex2())


test_ex2()
