"""
написать свою реализацию функции reduce() с описание в инлайновых и многострочных комментариях
ее работы.
def my_reduce(): моя реализация. (постарайтесь по памяти реализовать.)
"""

from functools import reduce


def my_reduce(function, sequence, initial=0):
    """ my_reduce(function, sequence[, initial]) -> value

        Applies a function that takes two arguments to the first two elements
        of a sequence. The result of the calculation is used as the first element
        for the calculation and the next element of the sequence as the second.

        Example:
        my_reduce(lambda x, y: x + y, [10, 50, 5, 6, 6, 8, 95, 602, 5665, 54])
        is a same to (((((((10+50)+5)+6)+6)+8)+...)+54)

        Initial argument is optional. If it fill function start with
        initial + sequence[0] and next use the logic described above.
    """

    iterator = iter(sequence)  # make iterator from sequence

    if initial == 0:  # if intial value is empty take second element to solving
        try:
            value = next(iterator)
        except StopIteration:
            pass
    else:   # if initial value exist use that like a first value
        value = initial

    for i in iterator:  # call function with variables from sequence
        value = function(value, i)

    return value


numbers: list = [10, 50, 5, 6, 6, 8, 95, 602, 5665, 30, 54]

my_fun_1 = my_reduce(lambda x, y: x + y, numbers)

my_fun_2 = reduce(lambda x, y: x + y, numbers)

print(my_fun_1, my_fun_2)


