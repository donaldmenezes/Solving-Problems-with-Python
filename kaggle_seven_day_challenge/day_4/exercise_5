def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    i = arrivals.index(name)
    if (len(arrivals)) % 2 == 1:
        n = int(len(arrivals)/2)
        if i > n and arrivals[-1] != arrivals[i]:
            return True
        else:
            return False
    else:
        n = int(len(arrivals)/2)
        if i >= n and arrivals[-1] != arrivals[i]:
            return True
        else:
            return False
            
            
# another solution

def fashionably_late(arrivals, name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
