"""
Реализовать любым способом патерн одиночка (singleton)
"""


class SingletonExample:
    """Class use like a singleton example"""

    def __new__(cls):
        if not hasattr(cls, 'obj'):
            my_obj = super(SingletonExample, cls).__new__(cls)
            cls.obj = my_obj
        return cls.obj


ex_1 = SingletonExample()
ex_2 = SingletonExample()

print(f'id1{id(ex_2)} id2{id(ex_1)}')
