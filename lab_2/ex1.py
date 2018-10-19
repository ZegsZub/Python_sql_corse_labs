# lab №2 ex. 1 | Var 4 Sergey Zubrilin 10/3/18


import math
from random import uniform
import numpy as np


class Metric:
    """
    Класс описываюший различные метрики
    """
    @staticmethod
    def manhattan(a, b):
        """
        ex1,d) Определить функцию manhattan(A, B) для нахождения манхэттенского
        расстояния между точками A и B.
        :param a: point_coordinates (two_elements_{list_or_tuple_or_array})
        :param b: point_coordinates (two_elements_{list_or_tuple_or_array})
        :return: float
        """
        return math.fabs(a[0] - b[0]) + math.fabs(a[1] - b[1])

    @staticmethod
    def metric_for_ex4(a, b):
        """
        ex4) Описывает заданную в ex4 метрику
        :param a: point_coordinates (two_elements_{list_or_tuple_or_array})
        :param b: point_coordinates (two_elements_{list_or_tuple_or_array})
        :return: float
        """
        return min(math.fabs(a[0]-b[0]), math.fabs(a[1]-b[1]))


class MatrixTool:
    def __init__(self):
        """
        При инициализации, дабовляеться два пустых столбца в матрицу (для задание b, c и создает массив
        записей производный от исходной матрицы
        """
        dtype = [('X', float), ('Y', float), ('O', float), ('coordinate quarter', int)]
        self.matrix_ex1 = np.array([self.random_point_in_square() for _ in range(4)], dtype=np.float16)
        self.matrix = np.array([tuple(el) for el in np.hstack((self.matrix_ex1,
                                0*np.ones((self.matrix_ex1.shape[0], 2)))).tolist()], dtype=dtype)
        self.r_matrix = self.random_matrix()

    @staticmethod
    def random_point_in_square(side=2):
        """
        функция, генерирующая случайные координаты точек входяшии в
        квадрат. Функция возвращает list из вдвух значений float [float(), float()] в случае если условие |x| + |y| <= d
        возваращает True.
        """
        point = [uniform(-side / 2, side / 2) for _ in range(2)]

        return point

    @staticmethod
    def random_matrix(start=0, stop=10, i=10, j=10):
        """
        generate random matrix
        :param start: int
        :param stop: int
        :param i: int
        :param j: int
        :return: numpy.ndarray
        """
        return np.array([[np.random.randint(start, stop) for _ in range(i)] for _ in range(j)])

    def sort_by_max_range(self):
        """
        b)"Отсортировать точки в порядке возрастания расстояния от центра
           квадрата."
        подсчитывает ростояние от точки до начала координат и сотрирует по возрастанию (по этому расстоянию)
        """
        for i in range(len(self.matrix)):
            self.matrix[i][2] = math.sqrt(self.matrix[i][1]**2 + self.matrix[i][0]**2)
        self.matrix = np.sort(self.matrix, order='O')

    def nearest_to_center(self):
        """
        a) "Найти точку, ближайшую к центру квадрата."
        :return: tuple.
        """
        self.sort_by_max_range()
        return self.matrix[0]

    def sort_by_coordinate_quarter(self):
        """
            Определяет координатнуй четверть входных точек.
        """
        for i in range(len(self.matrix)):
            if self.matrix[i][0] > 0 and self.matrix[i][1] > 0:
                self.matrix[i][3] = 1
            elif self.matrix[i][0] < 0 < self.matrix[i][1]:
                self.matrix[i][3] = 2
            elif self.matrix[i][0] < 0 and self.matrix[i][1] < 0:
                self.matrix[i][3] = 3
            elif self.matrix[i][0] > 0 > self.matrix[i][1]:
                self.matrix[i][3] = 4
            else:
                self.matrix[i][3] = 0

    def coordinate_quarter(self, quarter=1):
        """
            с) "Профильтровать массив, оставив только точки из первого квадранта.
        """
        res = np.array(list(filter(lambda x: x[3] == quarter, self.matrix)))
        # думал написать что-то вроде "if res: return res" но не вышло, так как в numpy подобная структура для масивов
        # состоящих больше чем из двух элементов неопределена :
        # {https://stackoverflow.com/questions/10062954/valueerror-the-truth-value-of-an-array-with-more-than-one-element-is-ambiguous}
        # советуют использовать метод .all() или .any() но они не работают с "structured arrays"(массивами записей)
        # так что я не придумал ничего лучше чем это ->
        try:
            res[0]
            return res
        except IndexError:
            return f'Not point in {quarter} coordinate quarter'

    def range_matrix(self, metric=Metric.manhattan):
        """
        Возврашает матрицу растояний в заданной метрике
        """
        l = len(self.matrix)
        range_matrix = np.zeros(shape=(l, l))
        count = 0
        for i in range(count, l):
            count += 1
            for j in range(count, l):
                range_matrix[i, j] = metric(self.matrix[i], self.matrix[j])

        return range_matrix + range_matrix.T

    def nearest_or_farthest_point(self, range_matrix, mod='nearest'):
        """
        e) В исходном массиве найти пару точек, наиболее близких в смысле
        манхэттенской метрики.
        :param metric: method of class Metric
        :param mod: 'farthest' or 'nearest'
        :return: ближайшие точки по манхэттанской метрике
        """
        if mod == 'nearest':
            count = 0
            l = len(self.matrix)
            min = float('inf')
            min_range_coord_index = []
            for i in range(count, l):
                count += 1
                for j in range(count, l):
                    if range_matrix[i, j] < min:
                        min_range_coord_index = [i, j]
                        min = range_matrix[i, j]
            return self.matrix[min_range_coord_index]

        if mod == 'farthest':
            count = 0
            l = len(self.matrix)
            max = 0
            max_range_coord_index = []
            for i in range(count, l):
                count += 1
                for j in range(count, l):
                    if range_matrix[i, j] > max:
                        max_range_coord_index = [i, j]
                        max = range_matrix[i, j]
            return self.matrix[max_range_coord_index]


def test_ex1():

    res = MatrixTool()
    print(res.matrix)
    print('a)------------------nearest_to_center_point-------------------')
    print(res.nearest_to_center())
    print('b)----X------------Y-------------O--------quarter-------------')
    res.sort_by_max_range()
    print(res.matrix)
    print('_)----X------------Y-------------O--------quarter-------------')
    res.sort_by_coordinate_quarter()
    print(res.matrix)
    print('c)-----------------first_coordinate_quarter_points-------------')
    print(res.coordinate_quarter())
    print('d)-----------------manhattan_range_matrix----------------------')
    print(res.range_matrix(metric=Metric.manhattan))
    print('e)-----------------nearest_point_by_manhattan_metric-----------')
    print(res.nearest_or_farthest_point(res.range_matrix()))


test_ex1()






