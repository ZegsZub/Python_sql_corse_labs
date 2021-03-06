# Отчет по второй лабораторной работе
## Сергей Зубрилин VAR 4
>Задание № 1:
````
1. Даны 10 случайных точек пространства 2ℝ , лежащих внутри квадрата со
стороной 2 с центром в начале координат.

a. Найти точку, ближайшую к центру квадрата.
b. Отсортировать точки в порядке возрастания расстояния от центра
квадрата.
c. Профильтровать массив, оставив только точки из первого квадранта.
d. Определить функцию manhattan(A, B) для нахождения манхэттенского
расстояния между точками A и B. Это расстояние определяется по
формуле: **.
e. В исходном массиве найти пару точек, наиболее близких в смысле
манхэттенской метрики.
````
**Код решения: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_2/ex1.py)**

**Код тестировки: [GitHub page]()**
###
>Задание № 2:
Зависит от класса MatrixTool from ex1
````
2. Cконструировать блочную матрицу (используя функции для заполнения
стандартных матриц) и применить функции обработки данных и поэлементные
операции для нахождения заданных величин.
                               5
 [ 1  1  1 -1 -1 -1]       S = Σ  a₍ii₎³
 [ 1  1  1 -1 -1 -1]          i=0
 [ 1  1  1 -1 -1 -1]
 [ 2  2  2  3  0  0]
 [ 2  2  2  0  3  0]
 [ 2  2  2  0  0  3]
````
**Код решения: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_2/ex2.py)**

**Код тестировки: [GitHub page]()**
###
>Задание № 3:
Зависит от класса MatrixTool from ex1
````
3. Написать функцию, проверяющую по критерию Сильвестра, является ли
матрица положительно определённой. Проверить работу функции на следующих
матрицах:
    [ 7  6  5  6  8]
    [ 6  7  0  4  3]
  A=[-2  7  6 -3 -1]
    [ 2  0  5  4  7]
    [ 8 -2  3  1  3]

    [-3  8  9 -2  0]
    [ 3 -5  2 -5  5]
  B=[ 3  7  2  7  3]
    [-3  4  7 -4  6]
    [ 9  9  3 -3  6]
````
**Код решения: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_2/ex3.py)**

**Код тестировки: [GitHub page]()**
###
>Задание № 4:
Зависит от класса MatrixTool from ex1
````
4. При решении многих задач транспортной логистики возникает необходимость
в построении матрицы расстояний между объектами. Попробуем решить эту
подзадачу в NumPy.
Сгенерировать 10 случайных точек на плоскости. Пусть, для определённости,
эти точки попадают в квадрат, ограниченный прямыми x=0, y=0, x=10, y=10 .
Необходимо построить матрицу попарных расстояний между ними, если в качестве
расстояния выбрана следующая метрика p(A,B) = min {|Xa - Xb|,|Ya - Yb|} .
На основе этой матрицы найти 2 наиболее удалённые (в указанной метрике)
точки.
````
**Код решения: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_2/ex4.py)**

**Код тестировки: [GitHub page]()**
###
>Задание № 5:
````
5. Написать функцию, которая заменяет положительные элементы вектора
суммой всех его отрицательных элементов. Функция считывает вектор из файла
input.csv и записывает результирующий вектор в файл output.csv.
````
**Код решения: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_2/ex5.py)**

**Код тестировки: [GitHub page]()**
###
>Дополнительное задание ЛР2:
````
Написать функцию, реализующую метод отражений решения СЛАУ
Ax=b. Проверить работу функции на примерах. Сравнить со стандартной
функцией решения СЛАУ.
````
**Код решения: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_2/dop_task.py)**

**Код тестировки: [GitHub page]()**

