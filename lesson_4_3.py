"""
4.3 Переопределение методов в Python
"""
class Person:

    name = 'adam'

    def walk(self):
        print('Человек ходит')

    def breathe(self):
        print('Человек дышит')

class Doctor(Person):

    name = 'Ivan'

    def breathe(self):
        print('Доктор дышит')

p = Person()
d = Doctor()
p.breathe()
d.breathe()
p.walk()
d.walk()
print(p.name, d.name)


