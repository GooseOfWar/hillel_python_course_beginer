"""
file for class in task 4
"""


class Visibility():
    """Class used to return visibility area"""
    def __init__(self, val_1, val_2):
        self.mul = val_2 * val_1

    def local_vis(self):
        return locals()

    def vars_vis(self):
        return vars(self)
