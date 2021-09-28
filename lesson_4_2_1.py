"""
4.2 Наследование от object и от других встроенных типов
"""
class Person:
    pass

class Doctor(Person):
    pass

class Architect(Person):
    pass

class Mylist(list):
    pass


print(issubclass(Person, object))
print(issubclass(Doctor, object))
print(dir(object))
print(dir(Person))
p = Person()
print(p.__str__())
d = Doctor()
print(d.__str__())