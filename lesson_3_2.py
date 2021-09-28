"""
Магические методы __len__ и __abs__
"""

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name) + len(self.surname)


a = Person('asder', 'fresd')
print(a)
print(len(a))

class peace_of_line:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self.x2 - self.x1)

    def __abs__(self, d):
        return abs(d)

pl = peace_of_line(9, 3)
print(pl)
print(len(pl))
