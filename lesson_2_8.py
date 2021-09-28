"""

"""
class Square:

    def __init__(self, s):
        self.__side = s
        self.__area = None
        self.__perimetr = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None
        self.__perimetr = None

    @property
    def area(self):
        if self.__area is None:
            print('Calculate area')
            self.__area = self.side ** 2
        return self.__area

    @property
    def perimetr(self):
        if self.__perimetr is None:
            print('Calculate perimetr')
            self.__perimetr = self.side * 4
        return self.__perimetr

a = Square(5)
print(a.area)
print(a.perimetr)
a.side = 19
print(a.area)
print(a.perimetr)