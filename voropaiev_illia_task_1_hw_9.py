"""Сделать пример всех функций которых мы изучили."""
from typing import Any

# all and any examplees
example_int_comparison: bool = 4 != (2 + 2)
example_str_comparison: bool = "loshadka" == "Loshadka".lower()
example_iterable: tuple = (example_int_comparison, example_str_comparison, True)

example_all: bool = all(example_iterable)
example_any: bool = any(example_iterable)

print(example_all)
print(example_any)
print(any([]))
print(all([]))

# filter and map exampes
list_of_strings: list = ['one', 'two', 'list', '', 'dict', '100', '1', '50']
filtered_list_of_strings: list = list(filter(str.isdigit, list_of_strings))
print(list(filter(str.isdigit, list_of_strings)))

list_of_words = ['one', 'two', 'list', '', 'dict']

print(list(map(str.upper, list_of_words)))  # ['ONE', 'TWO', 'LIST', '', 'DICT']
print(list(map(str.isdigit, list_of_strings)))
# [False, False, False, False, False, True, True, True]

print(list(map(lambda x: int(x), filtered_list_of_strings)))  # Use the lambda expression
print(list(map(int, filtered_list_of_strings)))  # simplified variant


# something like factory method i'm not sure
def goose() -> Any:
    """Goose function. Always return Ga Ga Ga"""
    return "Ga Ga Ga "


def grany_factory() -> Any:
    """Function Granny call Goose"""
    return goose


grany_call_goose = grany_factory()
print(grany_call_goose())


# Factory method
def battle_decorator(fun) -> Any:
    """Decorator function. Add Batlle сry"""

    def wraper() -> Any:
        my_fun = fun()
        batle_cry = "Gaaaa, I'll eat your face"
        return my_fun + batle_cry

    return wraper


@battle_decorator
def goose() -> Any:
    """Goose function. Always return Ga Ga Ga"""
    return "Ga Ga Ga "


print(goose())
