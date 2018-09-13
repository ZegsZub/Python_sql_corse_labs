from random import choice
from string import ascii_letters
import operator


def filling_random_sym():
    with open('test_logs/log.txt', 'w') as log_file:
        for el in range(10):
            log_file.writelines(''.join(choice(ascii_letters) for i in range(20)))
            log_file.write('\n')


def text_analysis():
    with open('test_logs/log.txt', 'r') as log_file:
        all_el = ''.join([x[:-1] for x in log_file.readlines()])
        unique_el = {el: 0 for el in all_el}

        for el in all_el:
            unique_el[el] = unique_el.get(el) + 1

        sum_of_el = sum([x[1] for x in unique_el.items()])
        max_el = max(unique_el.items(), key=operator.itemgetter(1))
        rel_val = max_el[1] / sum_of_el

        return [max_el[0], max_el[1], rel_val]


# filling_random_sym()
print(text_analysis())
