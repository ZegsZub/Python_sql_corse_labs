# lab №1 ex. 1 | Var 9 Sergey Zubrilin 9/13/18


import math


def ex1(eps = 0.001):
    n = 2
    res = 1
    temp = 1
    flag = True
    while flag:
        res *= 1-(2/(n*(n+1)))
        if math.fabs(res-temp) < eps:
            flag = False
        n += 1
        temp = res
    return res


print(ex1())
