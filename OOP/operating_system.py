class OperatingSystem:
    multitasking = True
    name = "Mac OS"
    
class Apple:
    website = "www.apple.com"
    name = "Apple"
    
class Macbook(Operating System, Apple):
    def __init__(self):
        if self.multitasking == True:
            print("This is a multitasking system. Visit {} for more details.".format(self.website))
            print("Name: " self.name)
            

macbook = Macbook()
