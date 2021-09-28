"""
 Создайте класс Laptop, у которого есть:
конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука. На основании этих аргументов нужно
для экземпляра создать атрибуты brand, model, price и также атрибут laptop_name - строковое значение, вида "<brand> <model>"
hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"
И затем создайте 2 экземпляра класса Laptop и сохраните их в переменные laptop1 и laptop2.
"""
class Laptop():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'

laptop1 = Laptop('dell', 'x5', 100000)
laptop2 = Laptop('asus', 't3', 100000)

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"