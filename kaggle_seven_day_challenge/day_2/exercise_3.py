def to_smash(total_candies, num = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between num friends. If no argument is given for num, 
    num assumes its value to be 3.
    
    >>> to_smash(91)
    1
    """
    
    return total_candies % num
