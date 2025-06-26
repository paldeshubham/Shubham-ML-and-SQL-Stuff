
class ATM:
    def __init__(self, balance):
        self.balance = balance

    
    def withdraw(self, amount, fee=0):
        if self.balance >= (amount + fee):
            self.balance -= (amount + fee)
            return f"Withdrew {amount}. Remaining balance: {self.balance}."
        else:
            return "Insufficient funds."


atm = ATM(1000)


print(atm.withdraw(200))            
print(atm.withdraw(200, 10))        