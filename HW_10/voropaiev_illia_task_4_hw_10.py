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

# Dict used like a memory. Process in a cycle will be saved on it
memory_dict: dict = {}

# Cycle use for program regular working
while True:
    # user input converted to the list with .split method
    user_args: list = input("Input your args for summing\n").split()
    if user_args == ['q']:  # if input = q program will stop
        print('Good bye')
        break

    args_list = list(map(int, user_args))   # arguments from input convert to the int
    args_tuple: tuple = tuple(args_list)    # list with int args convert to the tuple because tuple is hashable


    def check_agrs_decorator(fun):
        """Function used like a decorator.
        Compare arguments with previous arguments.
        If arguments already exist function get value from memory dict.
        In another case function use another function for solving sum"""

        def wrapper(n_arg: tuple) -> int:
            """Wrapper"""

            if n_arg in memory_dict:
                print("These arguments are already used".center(150, '_'))
                return memory_dict[n_arg]

            print("New args!".center(150, '_'))
            return fun(n_arg)

        return wrapper


    @check_agrs_decorator
    def hash_args(args: tuple) -> int:
        """Function summing digital value and write value and results to the memory"""
        memory_dict[args] = sum(args)
        return sum(args)


    print(hash_args(args_tuple))
