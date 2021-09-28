"""
4.7 Slots
"""
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(2, 3)
print(p1.x, p1.y)
print(p1.__dict__)
p1.z = 4
print(p1.__dict__)

p2 = PointSlots(5, 6)
print(p2.x, p1.y)
# print(p2.__dict__)
p2.z = 4
print(p2.__dict__)
