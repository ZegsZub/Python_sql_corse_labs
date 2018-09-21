# lab №1 ex. 2 | Var 9 Sergey Zubrilin 9/13/18


def is_prime(number):
    """Верно ли, что оставшееся число – простое?"""
    count = 0
    if number is None:
        raise AttributeError("wrong format data, attr 'number'")
    for i in range(number):
        if number % (i+1) == 0:
            count += 1
        if count > 2:
            return False

    return True


def first_odd(population):
    """ Найдите первую с конца нечётную цифру числа. «Зачеркните» все цифры, следующие за найденной."""
    reverse_population = str(population)[::-1]
    for i, el in enumerate(reverse_population):
        if int(el) % 2 != 0 and int(el) != 1:
            return int(reverse_population[i:][::-1])
    return None


def ex2(population = 1011494):
    f_odd = first_odd(population)

    if is_prime(f_odd):
        return True
    else:
        return False


print(f'Is Prime? - {ex2()}')
