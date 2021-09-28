"""
Геттеры и сеттеры, property атрибуты
"""
class BankAccount:

    @property
    def my_balance(self):
        return self._my_balance

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

#    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
#    my_balance = property()
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)

"""
a = BankAccount('Ivan', 100)
# print(a.__balance)
# print(a.__balance)
# a.balance = 'Hello'
# print(a.__balance)

b = BankAccount('Vasya', 1000)
print(b.get_balance())
b.set_balance(600)
print(b.get_balance())
# b.set_balance('Hello')
print(b.balance)
b.balance = 777
print(b.balance)
"""

g = BankAccount('Georg', 888)
print(g.my_balance)


