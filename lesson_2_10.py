"""
Пространство имен класса
"""
python_dev = 1
go_dev = 1
react_dev = 1

class DepartmentIT:
    python_dev = 3
    go_dev = 3
    react_dev = 3

    def make_backend(self):
        print('python and go')

    def make_frontend(self):
        print('react')

    def info1(self):
        print(python_dev, go_dev, react_dev)

    def info2(self):
        print(DepartmentIT.python_dev, DepartmentIT.go_dev, DepartmentIT.react_dev)

    def info3(self):
        print(self.python_dev, self.go_dev, self.react_dev)

    @property
    def info4(self):
        return(self.python_dev, self.go_dev, self.react_dev)

    @classmethod
    def info5(cls):
        print(cls.python_dev, go_dev, react_dev)

    @staticmethod
    def info6():
        print(DepartmentIT.python_dev, go_dev, react_dev)

it1 = DepartmentIT()
print(it1.python_dev, it1.go_dev, it1.react_dev)
it1.info1()
it1.info2()
it1.info3()
print(*it1.info4)
it1.info5()
it1.info6()


