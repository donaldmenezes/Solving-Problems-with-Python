planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line
    
# Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune
--------------------------------------------------------------------
multiplicands = (2, 2, 2, 3, 3, 5)      #Iterate over Tuple
product = 1
for mult in multiplicands:
    product = product * mult

print(product)

# 360
---------------------------------------------------------------------
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')
        
# HELLO
---------------------------------------------------------------------
# enumerate
# Given a list, enumerate returns an object which iterates over the indices and the values of the list.
# To see its contents as a list, we can call list() on it.

def double_odds(nums):
    for i, num in enumerate(nums):
        if num % 2 == 1:
            nums[i] = num * 2

x = list(range(10))
print(double_odds(x))

# [0, 2, 2, 6, 4, 10, 6, 14, 8, 18]
-------------------------------------------------------------------------
list(enumerate(['a', 'b']))

#[(0, 'a'), (1, 'b')]
------------------------------------------------------------------------
nums = [
    ('one', 1, 'I'),
    ('two', 2, 'II'),
    ('three', 3, 'III'),
    ('four', 4, 'IV'),
]

for word, integer, roman_numeral in nums:
    print(integer, word, roman_numeral, sep=' = ', end='; ')
    
# 1 = one = I; 2 = two = II; 3 = three = III; 4 = four = IV;
--------------------------------------------------------------------------
[planet for planet in planets if len(planet) < 6]

# ['Venus', 'Earth', 'Mars']
--------------------------------------------------------------------------
[planet.upper() + '!' for planet in planets if len(planet) < 6]

#['VENUS!', 'EARTH!', 'MARS!']
--------------------------------------------------------------------------
[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]

#['VENUS!', 'EARTH!', 'MARS!']
--------------------------------------------------------------------------

def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    return len([num for num in nums if num < 0])
    ## Reminder: in the day 3 exercise we learned about a quirk of Python where it calculates
    ## something like True + True + False + True to be equal to 3.
    #return sum([num < 0 for num in nums])

