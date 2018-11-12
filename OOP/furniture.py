class Furniture:
    def __init__(self):
        self._typeOfWood = "Teakwood"
    
class Chair(Furniture):
    def __init__(self):
        super().__init__()
        self.__numberOfLegs = 4
        
    def setWoodType(self, typeOfWood):
        self._typeOfWood = typeOfWood
        
    def displayChairSpecifications(self):
        print("This chair is made of {}, and has {} legs.".format(self._typeOfWood, self.__numberOfLegs))
        

chair = Chair()
print("would you like to change the type of wood from Teakwood? y/n")
userChoice = input()

if userChoice == "y":
    print("Enter the type of wood you would like you chair to be made of: ")
    typeOfWood = input()
    chair.setWoodType(typeOfWood)
    
chair.displayChairSpecifications()
