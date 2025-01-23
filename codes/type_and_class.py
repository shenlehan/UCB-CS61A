a = [1, 2]
b = {'a': 1, 'b': 2}
print(type(a))
print(type(b))

class Account:
    interest = 0.02

    def __init__(self, name):
        self.name = name
        self.balance = 0

tom_account = Account('Tom')
print(hasattr(tom_account, 'balance'))