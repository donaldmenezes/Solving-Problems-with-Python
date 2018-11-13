class CreditCard:
    
    def __init__ (self, customer, bank, accountNumber, creditLimit, balance = 0):
        self.customer = customer
        self.bank = bank
        self.accountNumber = accountNumber
        self.creditLimit = creditLimit
        self.balance = balance
        
    def get_customer(self):
        return self.customer
    
    def get_bank(self):
        return self.bank
    
    def get_accountNumber(self):
        return self.accountNumber
    
    def get_creditLimit(self):
        return self.creditLimit
        
    def get_balance(self):
        return self.balance
    
    def charge(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("price should be numeric.")
        elif price < 0:
            raise ValueError("price cannot be negative.")
        else:    
            if price + self.balance > self.creditLimit:
                return False
            else:
                self.balance += price
                return True    
        
    def makePayment(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("price should be numeric.")
        elif amount < 0:
            raise ValueError("price cannot be negative.")
        else:
            self.balance -= amount
