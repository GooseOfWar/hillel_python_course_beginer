"""
Ваша задача - создать декоратор для функции, которая принимает
неограниченное количество позиционных ХЕШИРУЕМЫХ элементов.

Декоратор добавляет следующий функционал:
Если функция уже вызвалась с такими аргументами - ваша функция должна вернуть результат
выполнения этой функции из памяти, а не вычислять его заного.
Если не вызывалась - вычислить результат, положить его в память, и вернуть.

Подсказка - тут вам пригодятся словари.
"""

# TODO: я не делал проверку ввода на содержание букв так как при проверке
#  дз показалось что это лишь лишний гемор для проверяющего
#  так как в задании это нет.

import json

# for hard memory realise use .json file
# operation_memory dict will be used for comparison new and existing data
# .json file use not use format tuple so need use two dict
# one dict (hard_memory) for rewriting json file, use str as a key
# next dict (operation_memory) use tuple format for operation in program

with open('task4_10.json', "r", encoding='ANSI') as json_file:
    operation_memory: dict = json.load(json_file)
    print(json.dumps(operation_memory, indent=2))  # show data in file

# hard memory dict coping operation dict from .json file
hard_memory: dict = operation_memory.copy()

# Cycle use for program regular working
while True:

    # user input converted to the list with .split method
    # user args will be saved as a key for hard_memory dict
    user_args: str = input("Input your args for summing\n")
    # operation list converted to the tuple and used for solving
    operation_args: list = user_args.split()

    if operation_args == ['q']:  # if input = q program will stop
        print('Good bye!')
        break
    # arguments from input convert to the int
    args_list = list(map(int, operation_args))
    # list with int args convert to the tuple because tuple is hashable
    args_tuple: tuple = tuple(args_list)


    def check_agrs_decorator(fun):
        """Function used like a decorator.
        Compare arguments with previous arguments.
        If arguments already exist function get value from memory dict.
        In another case function use another function for solving sum"""

        def wrapper(n_arg: tuple) -> int:
            """Wrapper"""

            if n_arg in operation_memory:
                print("These arguments are already used".center(150, '_'))
                return operation_memory[n_arg]
            # from .json file operation dict also receives str keys
            # because file read unformatted
            # for comparison used user_args as a key(because they have same key format - str)
            if user_args in operation_memory:  #TODO: тут был elif но pylint говорит лучше if
                print("These arguments are already used".center(150, '_'))
                return operation_memory[user_args]
            print("New args!".center(150, '_'))
            return fun(n_arg)

        return wrapper


    @check_agrs_decorator
    def hash_args(args: tuple) -> int:
        """Function summing digital value and write value and results to the memory"""
        operation_memory[args] = sum(args)
        hard_memory[user_args] = sum(args)
        return sum(args)


    print(hash_args(args_tuple))
# write new and read data form hard_memory dict to the file
with open('task4_10.json', "w", encoding='ANSI') as json_file:
    json.dump(hard_memory, json_file, indent=2)
