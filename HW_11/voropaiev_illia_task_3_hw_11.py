"""Написать функцию которая принимает от пользователя 2 аргумента и делит онин на другой.
при попытке деления на ноль вывести пользователю "ай яй яй делить на ноль можно не многим"
Все остальные исключения с поймать и вывести их значение в текстовом формате.
И в любом случае вывести. " I 'am happy that you learn python"
"""
from colorama import Fore, Style
from typing import Union

# take user input and convert to the list used .split
user_data_list: list = input("Enter number that should be divided\n").split()

# if user input 'q' cycle will stop
while 'q' not in user_data_list:

    # return massage if user input more then 2 value
    if len(user_data_list) > 2:
        print('Only first two value will be calculated\n')


    def devide_foo(arg_1: Union[int, float], arg_2: Union[int, float]) -> str:
        """Function  give 2 arg and devide first arg on second

            Example:
                def devide_foo(x, y)
                answer = x/y
                print(answer)
        """
        try:
            answer: float = round(float(arg_1) / float(arg_2), 4)
            print(answer)
        except ZeroDivisionError:
            print(Fore.RED + 'ай яй яй делить на ноль можно не многим\n')
        except ValueError as e:
            print(Fore.RED + f'Sorry but {e} try again')
        finally:
            return Fore.BLUE + 'I \'am happy that you learn python'.center(150, '_')

    try:
        print(devide_foo(user_data_list[0], user_data_list[1]))
        print(Style.RESET_ALL)
    except IndexError as e:
        print(Fore.RED + f'No no {e}, you shall have at least 2 value\n')
        print(Style.RESET_ALL)

    # user_data_list should be rewritten here because user may input 'q' for stop
    user_data_list: list = input("Enter number that should be divided\n").split()
