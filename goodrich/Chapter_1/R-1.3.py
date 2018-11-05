def minmax(data):
    '''
    Assumes data is a list.
    Returns min and max
    '''
    
    data_1 = data.copy()
    data_1.sort()
    return (data_1[0], data_1[-1])
    
    
data = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]
smallest, largest = minmax(data)
print('max = {}, min = {}'.format(largest, smallest))
