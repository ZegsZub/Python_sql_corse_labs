from random import randint
import numpy as np
from numpy import genfromtxt


def random_vector(r=10, n=10):
    """
    генерация случайного вектора, пространства n в диапазаное от -r до r
    """
    vector = np.array([randint(-r, r) for _ in range(n)], dtype='int')

    return vector


def write_vector_in_file(vector, file='input.csv'):
    """
    Записывает vector в файл
    """
    np.savetxt(file, vector, delimiter=',', fmt='%.1e')


def ex5(input_file='input.csv', output_file='output.csv'):
    """
    Функция считывает вектор из файла input.csv и
    записывает результирующий вектор в файл output.csv.
    """

    vector_from_inp = genfromtxt(input_file, delimiter=',')
    sum_of_negative = np.sum(vector_from_inp[(vector_from_inp < 0)])
    np.place(vector_from_inp, vector_from_inp > 0, sum_of_negative)
    np.savetxt(output_file, vector_from_inp, delimiter=',', fmt='%.1e')


# генерация случайной матрицы в инпут файл
# write_vector_in_file(random_vector())
ex5()
