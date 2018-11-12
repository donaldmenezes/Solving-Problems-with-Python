class Car():
    def __init__ (self):
        self.carFare = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}
        
    def displayFareDetails(self):
        print("Cost per day: ")
        print("Hatchback: $", self.carFare['Hatchback'])
        print("Sedan: $", self.carFare['Sedan'])
        print("SUV: $", self.carFare['SUV'])
        
    def calculateFare(self, typeOfCar, numberOfDays):
        return self.carFare[typeOfCar] * numberOfDays
        
        
car = Car()
while True:
    print('Enter 1 to display fare details')
    print('Enter 2 to rent a car')
    print('Enter 3 to exit')
    userChoice = int(input())
    if userChoice == 1:
        car.displayFareDetails()
    elif userChoice == 2:
        print('Enter the type of car you want to rent: ')
        typeOfCar = input()
        print('Enter the number of days you want to rent the car: ')
        numberOfDays = int(input())
        fare = car.calculateFare(typeOfCar, numberOfDays)
        print('Total payable amount: $', fare)
        print('Thank you!')
    elif userChoice == 3:
        break
