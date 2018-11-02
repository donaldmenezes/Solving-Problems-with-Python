def smallest_stringy_number(s1, s2, s3):
    """Return whichever of the three string arguments represents the smallest number.
    
    >>> smallest_stringy_number('1', '2', '3')
    '1'
    """
		
    mini = int(s1)
    for i in range(int(s2), int(s3)+1, int(s3)-int(s2)):
        if mini > int(i):
            mini = int(i)
    return str(mini)



#Kaggle Solution

def smallest_stringy_number(s1, s2, s3):
	return min(s1, s2, s3, key=int)
