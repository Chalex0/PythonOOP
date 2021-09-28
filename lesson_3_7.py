"""
3.7 Магический метод __call__
"""
from time import perf_counter

class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('Init object: ', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'наш обьект вызывался {self.counter} раз')

    def average(self):
        return self.summa / self.length

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'функция отработала за {finish-start}')
        return result
@Timer
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr *= i
    return pr

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

a = Counter()
a(2, 3, 6)
print(a.summa)
print(a.length)
print(a.average())

fact = Timer(fact)
print(fact)
print(fact(4))
#fib = Timer(fib)
#print(fib(10))
print(Timer(fib)(10))





