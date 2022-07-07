import datetime
from datetime import date

class My_account:

    account_name = "Oluoma Uchendu"
    account_number = "3016177582"
    bank = "FBN"

    def __init__(self, dob = datetime, balance = 100000, year = 0):
        self.balance = balance
        self.dob = dob
        self.type = ""
        self.year = year

    def withdraw (self, amount):
        if (amount > self.balance):
            print ("Insufficient funds")
        else:
            print ("Transaction successful")
            x = self.balance - amount
            print(f"Your new account balance is {x}Naira")
        self.balance -= amount

    def deposit(self, amount, number=account_number):
        print(f"You have successfully deposited {amount} to {number}")
        self.balance -= amount


    def transfer (self, amount, number=2224432123):
        print(f"{amount} Naira successfully transferred to {number}")
        self.balance -= amount


    def paybills(self, amount = 0, type = ""):
        if amount > self.balance:
            print(f"You cannot pay your {type} bill due to insufficient balance")
        else:
            print("Payment successful")
        self.balance -= amount

    def inquiries(self, dob = 1/1/1990, name = account_name):
        if (datetime.year - dob.year < 16):
            print ("Your account is a Student account")
        else:
            print("Your account is a standard account")

        print(f"Your account balance is {self.balance}")
        print(f"your account name is {name}")


    def close(self, year = 2020):
        if (datetime.year - year < 2):
            print("You are not eligible to close this account yet")
        else:
            print("Account successfully closed")



oluoma = My_account( "" ,5000000)
oluoma.paybills(5000, "nepa")
print(oluoma.paybills(5000, "nepa"))
print(oluoma.balance)
print(oluoma.dob)



class FooBar:
    def __init__(self):
        self.number = 42