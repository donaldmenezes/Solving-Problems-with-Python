def is_multiple(n, m):
    '''
    Return True if n is a multiple of m,
    else returns False
    '''
    try :
        return int(m) % int(n) == 0
    except ValueError:
        return ("the two numbers should be integer values")
        

m = input("Enter a number: ")
n = input("Enter a number: ")

print(is_multiple(n,m))
