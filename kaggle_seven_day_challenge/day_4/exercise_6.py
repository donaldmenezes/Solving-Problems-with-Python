def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    nums.append(0)
    nums = sorted(nums)
    return nums.index(0)
    
    
