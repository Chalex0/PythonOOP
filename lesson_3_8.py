"""
3.8 Полиморфизм в Python
"""
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_rect_area(self):
        return self.a * self.b

    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_area(self):
        return self.a ** 2

    def get_area(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r

    def get_sq_area(self):
        return 3.14 * self.r ** 2

    def get_area(self):
        return 3.14 * self.r ** 2


rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
print(rect1.get_rect_area(), rect2.get_rect_area())

sq1 = Square(5)
sq2 = Square(7)
print(sq1.get_sq_area(), sq2.get_sq_area())

circ1 = Circle(5)
circ2 = Circle(7)
print(circ1.get_sq_area(), circ2.get_sq_area())

figures = [rect1, rect2, sq1, sq2, circ1, circ2]
for figure in figures:
    print(figure.get_area())
