def norm(v):
    """
    Assumes V is a list of integers.
    Returns the Euclidean norm of a vector.
    
    >>>norm([4,3])
    5.0
    
    """
    
    sum = 0
    for x in v:
        sum = sum + x**2
        
    return (sum)**0.5
    ## return (sum([x**2 for x in v]))**0.5
    
    
def norm(p,v):
    """
    Assumes V is a list of integers.
    Returns the p-norm of a vector
    
    >>> norm(2, 4, 3)
    5.0
    """
    sum = 0
    for x in v:
        sum = sum + x**p
        
    return (sum)**(1/p)
    ## return (sum([x**p for x in v]))**(1/p)
