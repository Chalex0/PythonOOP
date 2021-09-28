"""
4.1 Принцип наследования в ООП
"""
class Person:                                 #Parent

    def can_walk(self):
        print('Я могу ходить')

    def can_breathe(self):
        print('Я могу дышать')

class Doctor(Person):                        #Subclass

    def can_cure(self):
        print('Я могу лечить')

class Architect(Person):                     #Subclass

    def can_build(self):
        print('Я могу построить здание')

d = Doctor()
d.can_walk()
a = Architect()
a.can_breathe()
print(issubclass(Doctor, Person))
print(isinstance(d, Person))
print(issubclass(Person, Architect))



