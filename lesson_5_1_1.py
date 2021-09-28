"""
5.1 Исключения в Python
"""
print('Hello1')
print('Hello2')
try:
    int('hello')
except ValueError:
    print('wrong type')
print('Hello3')
try:
    print('hello'[9])
except IndexError:
    print('wrong index')
print('Hello3')
print('Hello4')
print('Hello5')
print('Hello6')





