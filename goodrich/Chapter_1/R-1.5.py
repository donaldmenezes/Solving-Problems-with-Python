def sum_of_squares(num):
    '''
    Assumes num is a positive integer.
    returns the sum of squares of all integers less than num
    '''
    
    return sum([i**2 for i in range (num)])
    
num = int(input('Enter a positive integer: '))

if num <= 0:
    print('the number entered is non positive')
else:
    print(sum_of_squares(num))
