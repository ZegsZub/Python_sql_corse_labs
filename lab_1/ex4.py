# lab №1 ex. 4 | Var 9 Sergey Zubrilin 9/13/18


from random import choice
from string import ascii_letters


def filling_random_sym():
    with open('test_logs/log.txt', 'w') as log_file:
        for el in range(10):
            log_file.writelines(''.join(choice(ascii_letters) for i in range(20)))
            log_file.write('\n')


def text_analysis(file='test_logs/log.txt'):
    with open(file, 'r') as log_file:
        all_el = ''.join((x for x in log_file.readlines())).replace('\n', '')

        unique_el = {el: 0 for el in all_el}

        for el in all_el:
            if el != '\n':
                unique_el[el] = unique_el.get(el) + 1

        sum_of_el = sum([x[1] for x in unique_el.items()])

        for key, value in unique_el.items():
            unique_el[key] = f'{round(unique_el.get(key)/sum_of_el*100, 2)}%'
        return unique_el


def update_output_log(dic, file='test_logs/output_log.txt'):
    with open(file, 'a') as log_file:
        log_file.write('\n'.join((f'{key} --> {value} |' for key, value in dic.items()))+'\n')


# filling_random_sym()
update_output_log(text_analysis())
