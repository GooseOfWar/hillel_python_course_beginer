"""
Написать функцию которая будет принимать 3 аргумента (int) и находить максимум из них '''
"""

user_data: str = input('Fillup arguments. Use space as a separator\n')  # user input data
operating_data: list = list(user_data.split())  # convert user_data to list from str


def data_max(*args: str) -> str:  # return max args
    return max(args)


print(data_max(operating_data[0], operating_data[1], operating_data[2]))  # print the result
