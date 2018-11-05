def sum_of_squares(num):
    '''
    Assumes num is a positive integer
    Returns the sum of squares of all odd positive integers smaller than num.
    '''
    
    empty_list = []
    for i in range(1,num,2):
        empty_list.append(i**2)
        
    return sum(empty_list)
    
num = int(input('Enter a positive number: '))

while num <= 0:
    print('the number entered is non positive')
    num = int(input('Enter a positive number: '))

print(sum_of_squares(num))
