"""
Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.
Затем используя функцию1  (вызвать ее) написать функцию 2
которая будет принимать 3 аргумента и находить максимум
с помощью функции 1.
в итоге будет .

псевдокод
функция_нахождения_макс_из_2х(арг1, арг2):
return максимальное значение из 2х аргументов

функция_нахождения_макс_из_3х(арг1, арг2, арг3):
использую тут функция_нахождения_макс_из_2х()
return максимальное значение из 3х аргументов.
"""

# user data input
user_data: list = input('Fillup three numbers. Use space as a separator.\n').split()
# user_data = ['55', '111', '6']
"""
check for data compatibility user_data shall contain 3 arguments and all argument
are numbers for start checking all criteria are False
"""
quantitative: bool = False  # quantitative criteria checks how many arguments are in list user_data
all_numbers: bool = False  # all_numbers criteria check for all data in list is digit

while not all([quantitative, all_numbers]):  # Work while all criteria not True
    # If list length less than 3 - error message and input again
    if len(user_data) < 3:
        user_data: list = input('Data shall three numbers. '
                                'Try again and use space as a separator.\n').split()
    else:
        quantitative: bool = True  # quantitative criteria is True if OK

    # If data isn`t digit - error message and input again
    if not all(i.isdigit() for i in user_data):
        user_data: list = input('Data shall be only digit. '
                                'Try again and use space as a separator.\n').split()
    else:
        all_numbers: bool = True  # all_numbers criteria is True if OK

# create operating_data list with converted data in int
operating_data: list = [int(i) for i in user_data]


def max_form_2(arg_1: int, arg_2: int) -> int:
    """Function return the max arg from 2 args"""
    return max(arg_1, arg_2)


def max_from_3(arg_1: int, arg_2: int, arg_3: int) -> int:  # return the max arg from 3 args
    """Function return the max arg from 3 args comparing two arguments"""
    return max(
        max_form_2(arg_1, arg_2),  # comparison the first 2 arg with last 2 args and return max
        max_form_2(arg_2, arg_3)
    )


print(max_from_3(operating_data[0], operating_data[1], operating_data[2]))  # print the result
