"""
3.9 Методы __getitem__ , __setitem__ и __delitem__
"""
class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Индекс за границами коллекции')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Индекс за границами коллекции')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границами коллекции')


v = Vector(1, 2, 3, 5, 10, 21, 13)
print(v)
v[2] = 6
print(v)
del v[2]
print(v)