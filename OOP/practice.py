# create a class with properties in it and print them


class shubh:

    def __init__(self):
        self.name="Shubham"
        self.age = 12

    def __str__(self):
        return f" the name is{self.name} and age is {self.age}"

s=shubh()
print(s)


class Student:

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def print_method(self):
        return f"{self.name}"
s= Student("shubham",19)
print(s.print_method())



class ATM:
    def __init__(self, balance):
        self.balance = balance

    def display_balance(self):
        return f"Your current balance is {self.balance}."


class AdvancedATM(ATM):
    def __init__(self, balance, card_number):
        super().__init__(balance)
        self.card_number = card_number

    # Method overriding
    def display_balance(self):
        return f"Your balance is ${self.balance} and your card number is {self.card_number}."


atm = ATM(1000)
advanced_atm = AdvancedATM(1500, "1234-5678-9012-3456")

# Accessing methods
print(atm.display_balance())          
print(advanced_atm.display_balance()) 




      