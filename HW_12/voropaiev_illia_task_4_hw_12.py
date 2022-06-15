"""
Создать класс с методом которого можно будет возвращать область
видимости(local) созданного экземпляра класса.
В конструкторе(__init__) вашего класса пускай будут те параметры которые вы захотите.
"""

from file_for_class import Visibility

# Create the class examples
vis1 = Visibility(1, 2)
vis2 = Visibility(2, 4)

# print the result. Use locals and vars
print(vis1, vis1.local_vis())
print(vis2, vis2.vars_vis())

