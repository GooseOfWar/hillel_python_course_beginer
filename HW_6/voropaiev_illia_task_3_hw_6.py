"""
отсортировать словарь по ключам
"""
# Input data
my_dict: dict = {'Beer': "Piiivo", 'Bread': 'Hleb', 'Horse': 'Loshadka', 'Pig': 'Sviniuka'}  # created unsorted dict
print(my_dict)

# Create sorted dict. By dict methods convert my_dict in tuple line and sort by first element of each tuple.
# Then convert again in dict
my_sorted_dict: dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
print(my_sorted_dict)
