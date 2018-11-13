class CreditCard:
    
    def __init__ (self, customer, bank, accountNumber, creditLimit):
        self.customer = customer
        self.bank = bank
        self.accountNumber = accountNumber
        self.creditLimit = creditLimit
        self.balance = 0
        
    def get_customer(self):
        return self.customer
    
    def get_bank(self):
        return self.bank
    
    def get_accountNumber(self):
        return self.accountNumber
    
    def get_creditLimit(self):
        return self.creditLimit
    
    def charge(self, price):    
        if price + self.balance > self.creditLimit:
            return False
        else:
            self.balance += price
            return True    
        
    def makePayment(self, amount):
        self.balance -= amount
