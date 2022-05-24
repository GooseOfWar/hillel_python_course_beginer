"""
Удалить дубликаты из dictionary
пример
Before : {
'id1':{
        'name': 'Ruslan',
        'class': 1,
        'subjects' : {'Math', 'Algorithms', 'English'}},
'id2':{
        'name': 'Mark',
        'class': 2,
        'subjects' : {'Geometry', 'Java', 'Cooking'}},
'id3':{
        'name': 'Ruslan',
        'class': 1,
        'subjects' : {'Math', 'Algorithms', 'English'}}}
After:
{'id1':{
        'name': 'Ruslan',
        'class': 1,
        'subjects' : {'Math', 'Algorithms', 'English'}},
'id2':{
        'name': 'Mark',
        'class': 2,
        'subjects' : {'Geometry', 'Java', 'Cooking'}}
"""

# given data dict
my_dict: dict = {
    'id1': {
        'name': 'Ruslan',
        'class': 1,
        'subjects': {'Math', 'Algorithms', 'English'}},
    'id2': {
        'name': 'Mark',
        'class': 2,
        'subjects': {'Geometry', 'Java', 'Cooking'}},
    'id3': {
        'name': 'Ruslan',
        'class': 1,
        'subjects': {'Math', 'Algorithms', 'English'}}
}

# empty dict for operation
my_unique_dict: dict = {}

# Empty dict will be updated by Key and Values from given data dict if Values not exist in empty dict
[my_unique_dict.update({k: v}) for k, v in my_dict.items() if v not in my_unique_dict.values()]

print(my_unique_dict)  # print results