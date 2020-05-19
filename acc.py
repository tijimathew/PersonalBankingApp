"""
A bank account has an initial balance
cannot with

"""

class Account:

    def __init__(self, filepath, balance = 1000):
        self.filepath = filepath
        self.is_withdraw_success = False
        with open(filepath, 'r') as file:
            current_balance = file.read()
            if current_balance == "":
                self.balance = balance
            else: 
                self.balance = int(current_balance)

    def is_funds_available(self, amount):
        return self.balance >= amount

    def withdraw(self, amount):
        if self.is_funds_available(amount):
            self.balance -= amount
            self.commit()
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
    

class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
    
    def transfer(self, amount, recipient):
        if self.withdraw(amount + self.fee):
            recipient.deposit(amount)
            return True
        else:
            return False

print("Current balances are :")

john_checking = Checking("john.txt", 1)
print("John: %s " % john_checking.balance)

jack_checking = Checking("jack.txt", 1)
print("Jack: %s " % jack_checking.balance)

if john_checking.transfer(10, jack_checking):
    print("Transfer was completed. Current balances are :")
    print("John: %s " % john_checking.balance)
    print("Jack: %s " % jack_checking.balance)
else: 
    print("Transfer was NOT completed. Current balances are :")
    print("John: %s " % john_checking.balance)
    print("Jack: %s " % jack_checking.balance)
