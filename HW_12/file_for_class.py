"""
file for class in task 4
"""


# create class
class Visibility():
    """Class used to return visibility area and result of multiplication"""

    def __init__(self, val_1, val_2):
        self.mul = val_2 * val_1

    # method that use locals to see local vars
    def local_vis(self):
        return locals()

    # method that use vars to see local vars
    def vars_vis(self):
        return vars(self)
