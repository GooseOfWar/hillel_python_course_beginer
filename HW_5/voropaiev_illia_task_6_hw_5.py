"""
Написать примеры всех методов из set объекта.
Пример
set1 = {1,2,3}
# add
set1.add(4)
# update
set1.update([2,3,4,5])

add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update'
'isdisjoint', 'issubset', 'issuperset',
'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

my_set: set = {1, 'x', 'y', 'Loshadka'}

my_set_2: set = set(my_set.copy())

my_set.add('48')
print(my_set)

my_set_2.update(['Goose'])
print(my_set_2)

my_set.remove(1)
print(my_set)

print(my_set.symmetric_difference(my_set_2))

my_set_2.pop()
print(my_set_2)

my_set.difference(my_set_2)
print(my_set.difference(my_set_2))

my_set.discard('Loshadka')
print(my_set)

my_set_2.intersection_update(my_set)
print(my_set_2)

my_set |= my_set_2
print(my_set)


