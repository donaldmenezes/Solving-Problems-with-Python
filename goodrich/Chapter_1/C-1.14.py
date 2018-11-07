def oddproduct(data):
    """
    assumes data is a list of integers
    returns a boolean if the list has a distinct pair of numbers whose product is odd
    """
    
    datacopy = data.copy()
    datacopy = set(datacopy)
    odd = 0
    
    for i in datacopy:
        if i%2 != 0:
            odd += 1
        if odd == 2:
            return True
        
    return False
    
data = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]
print(oddproduct(data))
