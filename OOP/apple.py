class Apple:
    manufacturer = "Apple"
    contactWebsite = "www.apple.com/contact"
    
    def contactDetails(self):
        print("To contact us, log on to ", self.contactWebsite)
        

class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017
        
    def manufactureDetails(self):
        print("This Macbook is manufactured by {} in the year {}".format(self.manufacturer, self.yearOfManufacture))
        
        
macbook = Macbook()
macbook.manufactureDetails()
macbook.contactDetails()
