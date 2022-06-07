"""
Тема Кортеж и работа сним.
Удалить элемент из кортежа.
Входные данные: (1, 2, 3)
Результат: (1, 2)
"""

user_tuple: tuple = (1, 2, 3)  # existing tuple
user_list: list = list(user_tuple)  # convert tuple to list
user_list.remove(3)  # remove the 3rd element
user_tuple = tuple(user_list)  # convert back to tuple

print(user_tuple)  # print the results
