"""
Магические методы __add__, __mul__, __sub__ и __truediv__
"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented


b = BankAccount('Ivan', 1456)

print(b.balance)
b.balance += 44
print(b.balance)
print(b + 500)
print(b.balance)
