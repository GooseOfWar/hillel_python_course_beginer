"""
написать функцию, которая принимает в качестве аргументов два списка, а возвращает список,
состоящий из элементов этих двух списков, при чем первый элемент списка - первый элемент первого аргумента,
второй элемент списка - первый элемент второго списка, третий элемент - второй элемент первого списка,
четвертый - второй элемент второго аргумента и т.д.
т.е для аргументов [1, 2, 3] и [11, 22, 33] функция должна вернуть [1, 11, 2, 22, 3, 33].
Будет плюсом использование генераторов последовательностей для решения этой задачи.
"""

list_one: list = [j for j in range(1, 10)]  # first list generator
list_two: list = [k for k in range(11, 100, 11)]  # second list generator


def list_formatting(operation_list_1, operation_list_2):  # in first list input data from second list
    if len(operation_list_1) != len(operation_list_2):  # compare length of list if they are not equal print massage
        print('Lists length shall be equal!')
    else:   # if length is OK insert data from second list in first list in position 1,3,5, etc
        # second list index use division without remainder for iterator (1//2=0, 3//2=1, 5//2=2, etc)
        # range shall be double length of first list for sufficient diapason
        [operation_list_1.insert(i, operation_list_2[i // 2]) for i in range(1, (len(operation_list_2) * 2), 2)]

        print(operation_list_1)
        
        return opertion_list_1


list_formatting(list_one, list_two)
