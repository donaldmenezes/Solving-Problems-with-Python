def sum_of_squares(num):
    '''
    Assumes num is a positive integer.
    returns the sum of squares of all odd positive integers less than num
    '''
    
    return sum([i**2 for i in range (1,num,2)])
    
num = int(input('Enter a positive integer: '))

while num <= 0:
    print('the number entered is non positive')
    num = int(input('Enter a positive integer: '))

print(sum_of_squares(num))
