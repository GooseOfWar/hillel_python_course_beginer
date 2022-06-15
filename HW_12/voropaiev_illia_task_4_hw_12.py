"""
Создать класс с методом которого можно будет возвращать область
видимости(local) созданного экземпляра класса.
В конструкторе(__init__) вашего класса пускай будут те параметры которые вы захотите.
"""

from file_for_class import Visibility

vis = Visibility()


print(vis.some_f1(1, 2), vis.local_vis)
print(vis.some_f1(2, 4), vis.local_vis)

