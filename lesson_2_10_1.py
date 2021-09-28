"""

"""
from string import digits


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'abrakadabra'

    @property
    def secret(self):
        s = input("Введите пароль: ")
        if s == self.password:
            return self.__secret
        else:
            raise ValueError("Доступ закрыт")

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_number(value):
        for i in digits:
            if i in value:
                return True
        return False

    @staticmethod
    def popular_password(value):
        with open(r'password.txt') as file:
            file = file.read()
            if value not in file:
                return True
            return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if not 4 <= len(value) <= 12:
            raise ValueError("Длина пороля должена быть минимум 4 символа и не превышать 12")
        if not User.is_include_number(value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not User.popular_password(value):
            raise ValueError(f"Установите другой пароль этот пароль '{value}' не безопасен!")
        self.__password = value


login = passw = 'aaa1'
u = User(login, passw)
print(u.password)
