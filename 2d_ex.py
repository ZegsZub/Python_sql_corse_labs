# lab №1 ex. 2 | Var 9 Sergey Zubrilin 9/13/18

def is_prime(digit):
    if digit is None:
        print('Error -- wrong format data')

    if digit == 0:
        return False

    for i in (2, digit-1):
        if digit % i == 0:
            return False

    return True


def first_odd(population=1011474):
    for el in str(population)[::-1]:
        if int(el) % 2 != 0:
            return int(el)
    return None


def ex2():
    f_odd = first_odd()
    print('{0} - first odd element'.format(f_odd))
    if is_prime(f_odd):
        print('{0} is prime'.format(f_odd))
    else:
        print('Ell {0} is not prime'.format(f_odd))
    return None


ex2()
