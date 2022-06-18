"""
Сделать примеры в модуле.
@property, setter, deleter
"""


class ExClass:
    """ It's a training @property class"""

    def __init__(self, paremeter_1, parameter_2):
        self.parameter_1 = paremeter_1
        self.parameter_2 = parameter_2

    @property
    def my_magic_method(self):
        """Method do some things with parameters"""
        return f'I do some things with {self.parameter_1} and {self.parameter_2}!!!'

    @my_magic_method.setter
    def my_magic_method(self, value: list):
        self.parameter_1 = value[0]
        self.parameter_2 = value[1]

    @my_magic_method.deleter
    def my_magic_method(self):
        self.parameter_1 = None
        self.parameter_2 = None


ex_call = ExClass(1, 'str')

print(ex_call.my_magic_method)  # getter
ex_call.my_magic_method = [24, True]  # Setter
print(ex_call.my_magic_method)
del ex_call.my_magic_method  # deleter
print(ex_call.my_magic_method)
