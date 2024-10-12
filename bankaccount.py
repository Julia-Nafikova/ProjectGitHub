"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    balance: int

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def close(self):
        self.balance = 0

    # @property
    # def balance(self):
    #     return self.balance
    #
    # @balance.setter
    # def deposit(self, amount):
    #     self.balance + amount
    #
    # @balance.setter
    # def withdraw(self, amount):
    #     self.balance - amount




    # @balance.deleter



# код для проверки
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500
#
account.withdraw(200)
print(account.balance)  # 1300
#
account.close()
print(account.balance)  # 0
