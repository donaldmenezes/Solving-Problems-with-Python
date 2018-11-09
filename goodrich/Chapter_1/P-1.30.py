def count_divide_2(num):
    """
    Assumes num is a positive integer
    Returns the number of times num has to be divided by 2 to get a value less than 2
    
    >>> count_divide_2(10)
    3
    """
    
    i = 0
    while num > 1:
        num = num // 2
        i = i + 1
        
    return i
