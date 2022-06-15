"""
 написать функцию которая с помощью assert будет тестировать ваш самописный reduce
"""

from voropaiev_illia_task_2_hw_12 import my_fun_1, my_fun_2


def fun_comparison(fun_1, fun_2):
    """Function compare the result of executing two functions"""

    # if condition is not met show assert alert
    assert fun_1 == fun_2, 'Functions aren\'t equal!'
    return 'Functions are equal!'


print(fun_comparison(my_fun_1, my_fun_2))
