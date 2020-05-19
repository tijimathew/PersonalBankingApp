"""
A bank account has an initial balance
"""

class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        self.initial_value = 1000
        with open(filepath, 'r') as file:
            current_value = file.read()
            if current_value == "":
                self.balance = self.initial_value
            else: 
                self.balance = int(current_value)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
    

class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
    
    def transfer(self, amount):
        self.balance -= amount + self.fee

checking = Checking("balance.txt", 1)
checking.transfer(10)
checking.commit()
print(checking.balance)