"""
сложить словари в один.
использовать for и dict methods.
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
"""

# input data
first: dict = {1: 10, 2: 20}
second: dict = {3: 30, 4: 40}
third: dict = {5: 50, 6: 60}
fourth: dict = {7: 70, 8: 80}
fifth: dict = {9: 90, 10: 100}

# created list of dictionaries
my_dict_list: list = [
    first,
    second,
    third,
    fourth,
    fifth,
]

# Create empty dict new_dict. All data will be added here
new_dict: dict = {}

# Each dict in list added to new_dict
for i in my_dict_list:
    new_dict.update(i)

print(new_dict)  # print the result
