def positive_index(data,k):
    '''
    Assumes data is a list and k is negative integer.
    Returns an equivalent element of list at position k and 
    a positive index number of k.
    '''
    
    j = len(data) - abs(k)
    return (data[k], j)
    
data = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]
k = -15
print(positive_index(data, k))
