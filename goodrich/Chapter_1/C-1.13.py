def reverselist(data):
    """
    Assumes data is a list of integers.
    Returns a list whose integers are reversed.
    
    >>> reverselist([0,1,2,3,4])
    [4,3,2,1,0]
    """
    
    emptylist = []
    datacopy = data.copy()
    
    for i in data:
        emptylist.append(datacopy.pop())
        
    return emptylist
    

data = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]
print(reverselist(data))

##Another Solution

#data[::-1]
## this will not mutate the original list
