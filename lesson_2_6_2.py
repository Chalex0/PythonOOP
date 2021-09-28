"""
 Создайте класс UserMail, у которого есть:
"""
class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, mail):
        if mail.count('@') == 1 and mail[mail.index('@'):].count('.') > 0:
            self.__email = mail
        else:
            print('Ошибочная почта')

    email = property(fset=set_email, fget=get_email)

k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait

x = property()
print(x)