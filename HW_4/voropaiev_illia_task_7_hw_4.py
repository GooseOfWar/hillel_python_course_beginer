"""
Написать программу которая данный список кортежей переведет в список списков
Входные данные: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Результат: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
"""
my_list: list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]  # the list
my_new_list = []  # create new empty list

for i in my_list:  # each element in list of tuple should be converted in list type and added to new list
    my_new_list.append(list(i))
print(my_new_list)  # print the results
