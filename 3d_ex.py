# lab №1 ex. 3 | Var 9 Sergey Zubrilin 9/13/18

from random import randint


def random_matrix(n=15):
    matrix = [[randint(1, 10) for j in range(n)] for i in range(n)]
    return matrix


def ex_3(matrix):
    max_streak, streak, max_streak_line = 0, 0, 0

    for line in matrix:
        streak, temp = 1, float('Inf')

        for el in line:
            if el > temp:
                streak += 1
                if max_streak <= streak:
                    max_streak = streak
                    max_streak_line = line
            else:
                streak = 1

            temp = el

    return [max_streak, max_streak_line]


matrix = random_matrix()
print(matrix)
print(ex_3(matrix))
