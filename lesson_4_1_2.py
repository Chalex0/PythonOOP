"""
Ваша задача создать пустые классы Vehicle Car Plane Boat RaceCar, которые находятся в следующей иерархии:
"""
class Vehicle:
    def __init__(self):
        print('class Vehicle')

class Car(Vehicle):
    print('class Car')

class RaceCar(Car):
    print('class RaceCar')

class Plane(Vehicle):
    print('class Plane')

class Boat(Vehicle):
    print('class Boat')

