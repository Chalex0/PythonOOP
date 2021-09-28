"""

Вспомним нашего приятеля с предыдущих уроков: класс Vector.

Ваша задача создать класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
"""

class Vector:

    def __init__(self, *args):
        self.values = sorted(list(filter(lambda x: type(x) == int, args)))

    def __str__(self):
        return f"Вектор({', '.join(map(str, self.values))})" if self.values else "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*list(map(lambda x: x + other, self.values)))
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*list(map(lambda x, y: x + y, self.values, other.values)))
            else:
                print('Сложение векторов разной длины недопустимо')
        print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*list(map(lambda x: x * other, self.values)))
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*list(map(lambda x, y: x * y, self.values, other.values)))
            else:
                print('Умножение векторов разной длины недопустимо')
        print(f'Вектор нельзя умножать с {other}')

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"