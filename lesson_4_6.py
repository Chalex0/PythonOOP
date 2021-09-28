"""
4.6 Множественное наследование
"""
class Doctor:

    def can_cure(self):
        print('Я доктор, я умею лечить!')

class Builder:
    def can_build(self):
        print('Я строитель, я умею строить!')

class Person(Doctor, Builder):
#    def can_build(self):
#        print('Я человек, я тоже умею строить!')
    pass

p = Person()
p.can_cure()
p.can_build()
print(Person.__mro__)