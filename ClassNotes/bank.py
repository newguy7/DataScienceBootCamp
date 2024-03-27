class BankAccount():

    def __init__(self,account_number,name):
        self.account_number = account_number
        self.name = name
        self.balance = 0

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        self.balance = self.balance - amount

acc1 = BankAccount(1234, "John Doe")

print(f'Balance before deposit: {acc1.balance}')
acc1.deposit(1000)
print(f'Balance after deposit: {acc1.balance}')
acc1.withdraw(500)
print(f'Balance after withdrawal: {acc1.balance}')
print(f'Balance of {acc1.name}: {acc1.balance}')

acc2 = BankAccount(2345, "Mary Joe")
print(f'Balance of {acc2.name}: {acc2.balance}')