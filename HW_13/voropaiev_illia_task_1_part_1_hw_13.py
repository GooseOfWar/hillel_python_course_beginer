"""
Сделать примеры в модуле.
__call__
__repr__
"""


class ExClass:
    """Class get your turtle name and print name and weapon what they use"""
    TURTLES: dict = {'Leonardo': 'Swords', 'Raphael': 'Sai',
                     'Donatello': 'Bo', 'Michelangelo': 'Nunchaku'}

    def __init__(self, turtles_name):
        self.name = turtles_name

    def __call__(self, *args, **kwargs):
        Turtles: dict = ExClass.TURTLES
        return print(f'I\'m {self.name} and i prefer to use {Turtles[self.name]}')

    def __repr__(self):
        """Class work like:
            " f'I\'m {self.name} i prefer to use {Turtles[self.name]}' "
            """


Leo = ExClass('Leonardo')
Doni = ExClass('Donatello')
Raph = ExClass('Raphael')
Mike = ExClass('Michelangelo')
Leo()
Doni()
Raph()
Mike()

print(help(Leo))

"""Continued on the next Part"""
