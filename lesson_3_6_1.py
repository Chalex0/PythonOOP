"""
Магический метод __bool__
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return abs(self.x - self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0


p1 = Point(1, 5)
print(bool(p1))
p2 = Point(0, 0)
print(bool(p2))
p3 = Point(1, 2)
if p3:
    print('hello')
