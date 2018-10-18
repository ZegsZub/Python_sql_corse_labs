# lab №2 ex. 3 | Var 4 Sergey Zubrilin 10/15/18


import numpy as np
from lab_2.ex1 import MatrixTool
from lab_2.ex1 import Metric


def test_ex4():
    ex4 = MatrixTool()
    # 'Сгенерировать 10 случайных точек на плоскости.Пусть,
    # для определённости, эти точки попадают в  квадрат, ограниченный прямыми'
    ex4.matrix = MatrixTool.random_matrix(start=0, stop=10, i=2, j=10)
    print('случайная матрица по заданным критериям')
    print(ex4.matrix)
    # 'Необходимо построить матрицу попарных расстояний между ними, в заданной мтерике'
    print('матрица расстояний по заданным критериям')
    ex4.r_matrix = ex4.range_matrix(metric=Metric.metric_for_ex4)
    print(ex4.r_matrix)
    # На основе этой матрицы найти 2 наиболее удалённые (в указанной метрике) точки.
    print(ex4.nearest_or_farthest_point(range_matrix=ex4.r_matrix, mod='farthest'))


test_ex4()
