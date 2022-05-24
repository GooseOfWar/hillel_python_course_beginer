"""
Вернуть из dictionary все уникальные values.
Пример
Входные данные = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Результат = {'S001', 'S005', 'S007', 'S002', 'S009'}
Усложнение! +5 points
Вернуть ту же структуру.
После dictionary L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S005"}, {"V":"S009"},{"VIII":"S007"}]
"""

# given data kist
my_dict: list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                 {"VIII": "S007"}]
print(my_dict)  # print given data for comparison

my_list: list = []  # empty list will fillup unpacked dictionaries from given data list

for element in my_dict:  # each dict element in given data list convert to tuple
    element = element.items()
    for values in element:  # each element in all tuples write into my_list consequentially
        my_list.extend(values)


my_help_list: list = []  # help list to compare elements
my_new_list: list = []  # main list where results will be writen

# each second values will be checked for existing in help_list
# if they are not in new list will be writen previous to operation and operation variable
for i in range(1, len(my_list), 2):

    if my_list[i] not in my_help_list:
        my_help_list.append(my_list[i - 1])
        my_help_list.append(my_list[i])
        my_new_list.append({my_list[i - 1]: my_list[i]})

print(my_new_list)  # print results


