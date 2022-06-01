"""
написать программу которая будет создавать список методов из доступных методов питон объектов.
Под доступными подразумевается методы без подчеркиваний. Фунции dir()
т.е для объекта set должен быть список методов
"""

user_function: str = input('What function you want to check?\n"",(), {}, [], set()\n')  # user input type of function

if user_function == '[]':  # list case
    old_method_list: list = dir([])
    print('list')
elif user_function == '{}':  # dict case
    old_method_list: list = dir({})
    print('dict')
elif user_function == 'set()':  # set case
    old_method_list: list = dir(set())
    print('set')
elif user_function == '()':  # tuple case
    old_method_list: list = dir(())
    print('tuple')
else:
    old_method_list: list = dir('')  # str case
    print('str')

new_method_list: list = []  # empty list who will be fill by right methods

for i in old_method_list:   # Check all methods in dir. If methods don't start with "_" sign add it to new_method_list
    j = str(i).startswith('_')

    if j is False:
        new_method_list.append(str(i))

print(new_method_list)  # print results
