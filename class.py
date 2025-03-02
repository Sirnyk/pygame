from itertools import count


class Human:
    def __init__(self, age, height, weight):
        self.age = 10
        self.height = 150
        self.weight = 50

    def say_hello(self):
        print('Hello, I am', self.age, 'yeats old')

    def happy_dirthday(self):
        self.age += 1


John = Human(10, 150, 50)

Frank = Human(60, 170, 80)


class Car:
    def sound(self):
        print('beep')

    def long_sound(self):
        print('beep-beep')


car = Car()


class Button:
    def __init__(self):
        self.counter = 0

    def click(self):
        self.counter += 1

    def click_count(self):
        return self.counter

    def reset(self):
        self.counter = 0


a = Button()


class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self,amount):
        self.balance += amount

    def withdtaw(self,amount):
        self.balance -= amount

    def display_balance(self):
        return self.balance

        
