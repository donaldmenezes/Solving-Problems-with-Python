def distinctlist(data):
    """
    assumes data is a list of integers
    returns if all the elements of list are distinct
    """
    
    datacopy = data.copy()
    datacopy = set(datacopy)
    
    return len(datacopy) == len(data)
    

data = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]

print(distinctlist(data))
print(distinctlist(data[:9]))
