"""
1. Создать словарь с ключами от 11 до 20 включительно. Значения = квадраты ключей
Пример:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15:
225}
2. просуммировать все значения(values), делается в одну строку.(look build in functions)
"""

# crete new dict
new_dict: dict = {}

# fillup new_dict where Keys = all numbers in range 11 to 20. Values is squared keys.
for key in range(11, 21):
    values: int = key ** 2
    new_dict.update([(key, values)])

sum_of_val: int = sum(new_dict.values())  # Sum all values

print(sum_of_val)  # Print sum
print(new_dict)  # Print crated dict
