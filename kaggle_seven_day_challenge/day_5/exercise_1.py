def has_lucky_number(nums):
    """
    Assumes nums is a list 
    Returns whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    
    for num in nums:
        if num % 7 == 0:
            return True
    return False
