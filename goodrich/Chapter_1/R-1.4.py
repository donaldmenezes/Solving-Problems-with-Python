def sum_of_squares(num):
    '''
    Assumes num is a positive integer
    Returns the sum of squares of all positive integers smaller than num.
    '''
    
    empty_list = []
    for i in range(0,num):
        empty_list.append(i**2)
        
    return sum(empty_list)
    
num = int(input('Enter a positive number: '))

if num <= 0:
    print('the number entered is negative')
else:
    print(sum_of_squares(num))
