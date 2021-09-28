"""

"""
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get balance')
        return self.__balance

#    my_property_balance = my_balance
    @my_balance.setter
    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance

#    my_balance = my_property_balance.setter(set_balance)
#   my_balance = property(my_balance)

h = BankAccount('Vitya', 678)
print(h.my_balance)
h.my_balance = 987
print(h.my_balance)
