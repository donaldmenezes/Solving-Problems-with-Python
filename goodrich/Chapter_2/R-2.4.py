class Flower:
    
    def __init__ (self, name, numberOfPetals = None, price = None):
        self.name = name
        self.numberOfPetals = int(numberOfPetals)
        self.price = float(price)
        
    def get_name(self):
        return self.name
    
    def get_numberOfPetals(self):
        return self.numberOfPetals
    
    def get_price(self):
        return self.price
    
    def set_name(self, name):
        self.name = name
        
    def set_numberOfPetals(self, numberOfPetals):
        self.numberOfPetals = numberOfPetals
        
    def set_price(self, price):
        self.price = price
        
    def __str__(self):
        return "Flower: {} : {} : {}".format(self.name, self.numberOfPetals, self.price)
