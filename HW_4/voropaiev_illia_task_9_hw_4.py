"""
Тема Листы
Даны два списка элементов если хоть один елемент совпадает отпринтить True.
print(Тrue) не слово! а объект подставить.
"""

user_list1: str = input('Input List 1, use space as separator\n')  # input list 1 as a str
user_list2: str = input('Input list 2, use space as separator\n')  # input list 2 as a str

user_list1: list = user_list1.split(' ')  # translate in list
user_list2: list = user_list2.split(' ')

for i in user_list1:  # every i element with every j element should be compared
    for j in user_list2:
        if i == j:
            print(f'These lists have a same element {i}', True)  # if lists have same element show the text
        else:
            None  # None if lists haven't any coincidences
