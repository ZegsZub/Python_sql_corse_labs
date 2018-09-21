# lab №1 ex. 3(test) | Var 9 Sergey Zubrilin 9/21/18


from ex3 import random_matrix, ex_3
import unittest


class TestEx3(unittest.TestCase):

    def test_random_matrix_generator(self):
        """Проверка сгенерированного объекта"""

        matrix = random_matrix()
        self.assertTrue(isinstance(matrix, list))

        for i in range(len(matrix)):
            self.assertTrue(isinstance(matrix[i], list))

            for digits in range(len(matrix[i])):
                self.assertTrue(isinstance(digits, int))

    def test_ex_3(self):
        """
        Определить строку, в которой содержится максимально длинная цепочка чисел, идущих в порядке возрастания.
        Вывести номер строки и длину цепочки.
        """

        matrix_1_for_test = [[7, 10, 9, 7, 3], [10, 9, 9, 10, 8], [5, 5, 1, 2, 2], [3, 3, 6, 2, 9], [3, 5, 8, 7, 4]]
        matrix_2_for_test = [[3, 8, 9, 1, 10, 2, 2, 1, 8, 8], [6, 7, 9, 4, 4, 1, 1, 8, 2, 5],\
                             [3, 8, 1, 5, 2, 5, 3, 10, 9, 5], [8, 9, 5, 7, 1, 10, 5, 5, 7, 9],\
                             [6, 9, 1, 9, 5, 9, 2, 2, 7, 3], [3, 9, 5, 4, 4, 10, 3, 1, 10, 4],\
                             [6, 9, 3, 7, 7, 8, 1, 2, 6, 6], [8, 5, 1, 10, 5, 2, 8, 1, 8, 2],\
                             [1, 2, 6, 1, 7, 6, 6, 8, 4, 4], [5, 5, 6, 3, 3, 3, 3, 5, 6, 8]]

        self.assertEqual(ex_3(matrix_1_for_test), [3, [3, 5, 8, 7, 4]])
        self.assertEqual(ex_3(matrix_2_for_test), [4, [5, 5, 6, 3, 3, 3, 3, 5, 6, 8]])


if __name__ == '__main__':
    unittest.main()
