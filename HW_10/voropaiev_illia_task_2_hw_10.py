"""
Написать функцию которая будет у пользователя брать python обект в любом виде
и выводить все его не магические методы в списке.
и написать декторатор который будет выводить колличество методов в объекте.
Похожую задачу мы уже решали. Можете взять решение из предыдущей.
Но декоратор уже ваш полностью)

func(tuple())
[count, index]

@methods_amount
[count, index]
2
"""

# user input type of function
# user_object: str = input('What function you want to check?\n"",(), {}, [], set()\n')
user_object: str = '[]'


def quantity_in_list_decorator(fun):
    """Print the length of methods list"""

    def wrapper(arg):
        my_fun = fun(arg)
        quantity = len(my_fun)
        print(f'Quantity of unmagic methods  {quantity}')
        return my_fun

    return wrapper


@quantity_in_list_decorator
def methods_for_obj(called_object: str) -> list:
    """Function return list with unmagical methods for user object.
    Fuction can read only (), {}, [], set() and str"""

    if called_object == '[]':  # list case
        old_method_list: list = dir([])
        print('You object is list')
    elif called_object == '{}':  # dict case
        old_method_list: list = dir({})
        print('You object is dict')
    elif called_object == 'set()':  # set case
        old_method_list: list = dir(set())
        print('You object is set')
    elif called_object == '()':  # tuple case
        old_method_list: list = dir(())
        print('You object is tuple')
    else:
        old_method_list: list = dir('')  # str case
        print('str')

    # empty list who will be fill by right methods
    new_method_list: list = [i for i in old_method_list if not i.startswith('_')]

    # Check all methods in dir. If methods don't start with "_" sign add it to new_method_list
    # for i in old_method_list:
    #     if i != str(i).startswith('_'):
    #         new_method_list.append(str(i))
    return new_method_list


print(methods_for_obj(user_object),)  # print results
