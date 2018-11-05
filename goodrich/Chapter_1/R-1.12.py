import random

def choice(data):
    '''
    assumes data is a list of numbers
    returns a random numerical value in the list data
    '''
    
    return data[random.randrange(len(data))]
    
data = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]

print(choice(data))
