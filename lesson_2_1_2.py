"""

"""
class Cat:
    breed = 'pers'

    def hello(*args):
        print('Hello world from kitty', args)

    def show_breed(self):
        print(f'my breed is {self.breed}')

    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('Nothing')

    def set_value(self, value, age=5):
        self.name = value
        self.age = age



Cat.hello()
bob = Cat()
bob.hello()
print(bob)
walt = Cat()
walt.show_breed()
walt.breed = 'siam'
walt.show_breed()
bob.show_breed()
mary = Cat()

mary.name = 'Mary'
mary.show_name()
