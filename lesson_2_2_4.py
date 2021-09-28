"""
 Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы "Полоска белая",
 "Полоска черная", начиная именно с фразы "Полоска белая"
"""

class Zebra():

    def __init__(self):
        self.white = True

    def which_stripe(self):
        print('Полоска белая' if self.white else 'Полоска черная')
        self.white = not self.white

z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"