"""
4.8 Slots: свойства(property) и наследования
"""
class Rectangle:

    __slots__ = ('width', 'height')

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def perimetr(self):
        return (self.width + self.height) *2

    @property
    def area(self):
        return self.width * self.height


r = Rectangle(3, 4)
print(r.width, r.height)
print(r.perimetr, r.area)
