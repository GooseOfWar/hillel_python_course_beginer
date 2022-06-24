"""
here is example for import and hassatr
"""

from voropaiev_illia_task_1_hw_14 import Person

if __name__ == '__main__':
    if hasattr(Person, '__init__'):
        print(Person.__dict__)
    if hasattr(Person, 'year_from_birth'):
        my_person = Person.year_from_birth('Alex', 1997)
        print(my_person.age)
