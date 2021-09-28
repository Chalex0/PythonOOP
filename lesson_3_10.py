"""
3.10 Магические методы __iter__ и __next__
"""
class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

#    def __getitem__(self, item):
#        return self.surname[item]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        item = self.name[self.index]
        self.index += 1
        return item

igor = Student('Igor', 'Nikolaev', [3, 4, 5, 6, 3])
print(igor)
for i in igor:
    print(i)
