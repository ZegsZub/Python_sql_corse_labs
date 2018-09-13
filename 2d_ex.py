# lab №1 ex. 2 | Var 9 Sergey Zubrilin 9/13/18


def is_prime(number):
    count = 0
    if number is None:
        print('Error -- wrong format data')
    for i in range(number):
        if number % (i+1) == 0:
            count += 1
            print(count)
        if count > 2:
            return False

    return True


def first_odd(population=1011494):
    reverse_population = str(population)[::-1]
    for i, el in enumerate(reverse_population):
        if int(el) % 2 != 0:
            return int(reverse_population[i:][::-1])
    return None


def ex2():
    f_odd = first_odd()
    print('{0} - new number'.format(f_odd))
    if is_prime(f_odd):
        print('{0} is prime'.format(f_odd))
    else:
        print('El ({0}) is not prime'.format(f_odd))
    return None


ex2()
