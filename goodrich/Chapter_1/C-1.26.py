def related(a, b, c):
    """
    Assumes a, b, c are numbers
    returns true if a+b=c or a=b-c or a*b=c
    """
    return a+b==c or a==b-c or a*b==c
