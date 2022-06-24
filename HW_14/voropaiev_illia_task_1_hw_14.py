"""
Приклади використання static and classmethod.
hasattr
Спробувати імпортувати класс з одно модуля в інший.
"""

from datetime import date


class Person:
    """Demonstrate classmethod and staticmethod use age of person"""
    def __init__(self, name, age):
        self.name = name
        if age >= 121:
            self.age = 'You are not real'
        else:
            self.age = age


    @classmethod
    def year_from_birth(cls, name, year):
        """a class method to create a Person object by birth year"""
        return cls(name, date.today().year - year)


    @staticmethod
    def is_adult(age):
        """a static method to check if a Person is adult or not"""
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.year_from_birth('mayank', 1996)

if __name__ == '__main__':
    print(person1.age)
    print(person2.age)
    print(Person.isAdult(22))
