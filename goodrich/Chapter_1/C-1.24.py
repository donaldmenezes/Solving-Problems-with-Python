def count_vowels(string):
    """
    returns the number of vowels in a given string
    
    >>> count_vowels('abcdefghi'):
    3
    """
    
    vowel = 0
    
    for i in string:
        if i.lower() in 'aeiou':
            vowel = vowel + 1
        
    return vowel
    
    

## def count_vowels(word):
##     counts = {}.fromkeys(”aeiou”, 0) 
##     for char in word.lower(): 
##         if char in counts: 
##             counts[char] += 1 
##     return counts
