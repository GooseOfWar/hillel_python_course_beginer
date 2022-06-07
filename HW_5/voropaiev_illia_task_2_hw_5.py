"""
Дан список с повторяющимися значениями необходимо из него удалить все определенные значения используя while цикл.
Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все eg
Результат: ['bear', 'milk']
"""

my_list: list = ['bear', 'milk', 'egg', 'egg', 'egg', 'egg']

while 'egg' in my_list:  # delete all egg from my list
    my_list.remove('egg')

print(my_list)
