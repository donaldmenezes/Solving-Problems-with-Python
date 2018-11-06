def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    a = 0
    for i in range(len(meals)):
        if i<=len(meals)-2:
            if meals[i+1] == meals[i]:
                return True
            else:
                a += 1
    if a+1 == len(meals) or len(meals) == 0:
        return False
        
#def menu_is_boring(meals):
#    # Iterate over all indices of the list, except the last one
#    for i in range(len(meals)-1):
#        if meals[i] == meals[i+1]:
#            return True
#    return False
