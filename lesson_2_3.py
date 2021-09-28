"""

"""
class Point():

    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Точка с координатами ({self.x}, {self.y})')

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу Point')
        return ((another_point.x - self.x)**2 + (another_point.y - self.y)**2)**0.5


p3 = Point()
p3.move_to(4, 5)
p3.move_to(-90, 5)
print(p3.x, p3.y)
p3.print_point()
p4 = Point()
p4.move_to(-1, 2)
print(f'Distance {p4.calc_distance(p3)}')
print(Point.list_points[1].x)