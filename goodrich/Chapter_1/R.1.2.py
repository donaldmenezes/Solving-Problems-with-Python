def is_even(k):
    '''
    returns true if k is even
    '''
    
    try :
        k = abs(k)
        for i in range(0, k+1, 2):
            if i == k:
                return True
        return False
    except ValueError:
        print('the number should be an integer')
    
    
k = input("Enter a number to check if it is even: ")

print(is_even(k))
