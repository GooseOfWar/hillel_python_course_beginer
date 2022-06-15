"""
написать 3 примера генераторных функций с различными последовательностями
"""

# ___________________________ ITS JUST A SAMPLES. NO COMMENTS ___________________________

from functools import reduce

val_1 = 1
val_2 = 2
val_3 = 3
val_str_1 = ['shliapa', 'palto', 'jacket']
val_str_2 = ['koni', 'ryba', 'gooose']


def some_numbers():
    some_list = [i for i in range(1, 10)]
    return some_list


def some_animals(seq1: list, seq2: list):
    some_seq = seq1 + seq2
    return some_seq


def my_gen1():
    yield 1
    yield 2
    yield 3


def my_gen2():
    yield range(200)
    yield range(200, 2000)
    yield range(2000, 200_000)


def me_gen3(arg_1: list, arg_2: list):
    yield reduce(lambda x, y: x + y, [val_3, val_2, val_1])
    yield arg_2
    yield arg_1
    for i in range(len(arg_1)):
        yield f'k nam prishli {arg_1[i]} ih bylo {arg_2[i]}'


for i in me_gen3(some_animals(val_str_2, val_str_1), some_numbers()):
    print(i)
