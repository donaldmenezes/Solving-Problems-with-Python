numbers = {'one':1, 'two':2, 'three':3}
numbers['one']
# 1

numbers['eleven'] = 11
numbers
# {'eleven': 11, 'one': 1, 'three': 3, 'two': 2}

numbers['one'] = 'Pluto'
numbers
# {'eleven': 11, 'one': 'Pluto', 'three': 3, 'two': 2}

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial
# {'Earth': 'E',
#  'Jupiter': 'J',
#  'Mars': 'M',
#  'Mercury': 'M',
#  'Neptune': 'N',
#  'Saturn': 'S',
#  'Uranus': 'U',
#  'Venus': 'V'}

'Saturn' in planet_to_initial
# True

'Betelgeuse' in planet_to_initial
# False

#A for loop over a dictionary will loop over its keys

for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# one = Pluto
# two = 2
# three = 3
# eleven = 11

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
' '.join(sorted(planet_to_initial.values()))
# 'E J M M N S U V'

# The very useful dict.items() method lets us iterate over the keys and values of a dictionary simultaneously. 
# (In Python jargon, an item refers to a key, value pair)

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
    
# Mercury begins with "M"
#      Venus begins with "V"
#      Earth begins with "E"
#       Mars begins with "M"
#    Jupiter begins with "J"
#     Saturn begins with "S"
#     Uranus begins with "U"
#    Neptune begins with "N"   
