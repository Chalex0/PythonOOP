"""
4.5 Делегирование в Python
"""
class Person:

    def breathe(self):
        print('Человек дышит')

class Doctor(Person):

    def breathe(self):
        print('Доктор дышит')
        super().breathe()

p = Person()
d = Doctor()
p.breathe()
d.breathe()
