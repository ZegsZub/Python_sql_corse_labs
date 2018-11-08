# Отчет по четвертой лабораторной работе
## Сергей Зубрилин VAR 1
>Задание № 1:
````
1. По данным из файла brexit_sth.csv построить столбцовую диаграмму
количества людей, поддержавших brexit, относительно их возраста.
````
**dependency files: [brexit_sth.csv](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/brexit_sth.csv)**

**Код решения: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex1.py)**

**Диаграмма: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex1_bar.png)**
###
>Задание № 2:
````
2. К данным из файла filter1.xlsx добавить столбец Surplas (излишки), который
определяется следующим образом: по закону полагается 21 м 2 жилплощади на
каждого члена семьи (прописанного в квартире) плюс 10 м 2 на семью. Всё, что
свыше, считается излишками. Если излишков нет, значение Surplas в данной
строке должно равняться нулю.
Отобразить информацию о квартиросъёмщиках:
    1) имеющих льготы
    2) имеющих льготы и не имеющих излишков площади
    3) чей общий метраж превышает 100 м 2
    4) прописавшихся в период с 1950 г. по 1970 г.
    5) имеющих льготы и прописавшихся после 1960 года
    6) всех льготников, имеющих избытки площади, а также лиц, имеющих
       метраж менее 100 м 2 и прописанных до 1957 года
    7) выбрать всех лиц с излишками жилплощади более 50 м 2 и не имеющих
       льгот, а также лиц, прописавшихся в период с 1950 г. по 1970 г., общий
       метраж которых превышает 100 м 2
````

**dependency files: [filter1.xlsx](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/filter1.xlsx)**

**Код решения: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex2.py)**

**Html table for 2.1: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex2_1_table.html)**

**Html table for 2.2: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex2_2_table.html)**

**Html table for 2.3: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex2_3_table.html)**

**Html table for 2.4: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex2_4_table.html)**

**Html table for 2.5: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex2_5_table.html)**

**Html table for 2.6: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex2_6_table.html)**

**Html table for 2.7: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex2_7_table.html)**

###
>Задание № 3:
````
3. По данным из файлов students1.txt, students2.txt, students3.txt сделать вывод о
линейной зависимости между успеваемостью студентов по следующим
предметам, посчитав соответствующие коэффициенты корреляции оценок по
1) 3 семестрам математического анализа (MathAnalysis1, MathAnalysis2,
MathAnalysis3)
2) истории Украины и специальным языкам программирования
(HistoryOfUkraine, SpecialProgrammingLanguages)
````
**dependency files:
[students1.txt](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/students1.txt),
[students2.txt](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/students2.txt),
[students3.txt](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/students3.txt)**

**Код решения: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex3.py)**

###
>Задание № 4:
````
4. По данным из файлов 2008.csv.bz2 (или 2008_part.csv) и airports.csv,
выполнить следующие задания:
    1) Какая из причин отмены рейса (CancellationCode) была самой
        частой? (расшифровки кодов можно найти в описании данных)
    2) Найдите среднее, минимальное и максимальное расстояние, пройденное
        самолетом.
    3) Не выглядит ли подозрительным минимальное пройденное расстояние? В
        какие дни и на каких рейсах оно было? Какое расстояние было пройдено
        этими же рейсами в другие дни?
    4) Из какого аэропорта было произведено больше всего вылетов? В каком
        городе он находится?
    5) Найдите для каждого аэропорта среднее время полета (AirTime) по всем
        вылетевшим из него рейсам. Какой аэропорт имеет наибольшее значение
        этого показателя?
    6) Найдите аэропорт, у которого наибольшая доля задержанных при
        отправлении рейсов (DepDelay&gt;0). Исключите при этом из рассмотрения
        аэропорты, из которых было отправлено меньше 1000 рейсов.
````
**dependency files:
[2008_part.csv](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/2008_part.csv),
[airports.csv](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/airports.csv)**

**Код решения: [GitHub page](https://github.com/ZegsZub/Python_sql_corse_labs/blob/master/lab_4/ex4.py)**
###