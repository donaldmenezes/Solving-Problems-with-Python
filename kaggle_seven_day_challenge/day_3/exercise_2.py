def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion
    
#####################

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion
    
# kaggle solution:- return not (ketchup or mustard or onion)

###################

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    if ketchup and not mustard:
        return True
    elif mustard and not ketchup:
        return True
    else:
        return False
        
# kaggle solution: return (ketchup and not mustard) or (mustard and not ketchup)
