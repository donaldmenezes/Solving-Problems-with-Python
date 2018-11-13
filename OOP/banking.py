from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayAvailableBalance():
        return 0

class SavingsAccount():
    
    def __init__(self):
        self.savingsAccount = {}
    
    def createAccount(self, name, initialDeposit):
        print()
        self.accountNumber = randint(10000, 99999)
        self.savingsAccount[self.accountNumber] = [name, initialDeposit]
        print("Account Creation has been successful. Your account number is", self.accountNumber)
        print()
    
    def authenticate(self, name, accountNumber):
        print()
        if accountNumber in self.savingsAccount.keys():
            if name in self.savingsAccount[self.accountNumber][0]:
                print("Authentication successful.")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication not successful.")
                print()
                return False
        else:
            print("Authentication not successful.")
            print()
            return False
    
    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccount[self.accountNumber][1]:
            print("Insufficicent Balance")
            print()
        else:
            print("Withdrawal was successful")
            self.savingsAccount[self.accountNumber][1] -= withdrawalAmount
            self.displayAvailableBalance()
        
    def deposit(self, depositAmount):
        print()
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print("Deposit was successful")
        self.displayAvailableBalance()
        print()
    
    def displayAvailableBalance(self):
        print("Available Balance: ", self.savingsAccount[self.accountNumber][1])
        
        

savingsAccount = SavingsAccount()
while True:
    print()
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account.")
    print("Enter 3 to exit")
    userChoice = int(input())
    print()
    if userChoice == 1:
        print("Enter your name: ")
        name = input()
        print("Enter initial amount to be deposited: ")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
        print()
    elif userChoice == 2:
        print("Enter your account number: ")
        accountNumber = int(input())
        print("Enter your name: ")
        name = input()
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
        print()
        if authenticationStatus == True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to previous menu")
                userChoice = int(input())
                if userChoice == 1:
                    print()
                    print("Enter withdrawal amount: ")
                    withdrawalAmount = int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                    print()
                elif userChoice == 2:
                    print()
                    print("Enter amount to deposit: ")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                    print()
                elif userChoice == 3:
                    print()
                    savingsAccount.displayAvailableBalance()
                    print()
                else:
                    break
    else:
        break
