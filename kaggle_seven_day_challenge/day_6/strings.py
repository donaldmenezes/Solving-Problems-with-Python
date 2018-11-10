'Pluto\'s a planet!'
## "Pluto's a planet!"

triplequoted_hello = """hello
world"""
print(triplequoted_hello)
## hello
## world
   
# Indexing
planet = 'Pluto'
planet[0]
# 'P'

# Slicing
planet[-3:]
# 'uto'

# How long is this string?
len(planet)
# 5

# Yes, we can even loop over them
[char+'! ' for char in planet]
# ['P! ', 'l! ', 'u! ', 't! ', 'o! ']

# ALL CAPS
claim = "Pluto is a planet!"
claim.upper()
# 'PLUTO IS A PLANET!'

# all lowercase
claim.lower()
# 'pluto is a planet!'

# Searching for the first index of a substring
claim.index('plan')
# 11

claim.startswith(planet)
# True

claim.endswith('dwarf planet')
# False

words = claim.split()
words
# ['Pluto', 'is', 'a', 'planet!']

datestr = '1956-01-31'
year, month, day = datestr.split('-')
year, month, day
# ('1956', '01', '31')

'/'.join([month, day, year])
# '01/31/1956'

# Yes, we can put unicode characters right in our string literals :)
' 👏 '.join([word.upper() for word in words])
# 'PLUTO 👏 IS 👏 A 👏 PLANET!'

planet + ', we miss you.'
# 'Pluto, we miss you.'

planet + ", you'll always be the " + str(position) + "th planet to me."
# "Pluto, you'll always be the 9th planet to me."

"{}, you'll always be the {}th planet to me.".format(planet, position)
# "Pluto, you'll always be the 9th planet to me."

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)
# "Pluto weighs about 1.3e+22 kilograms (0.218% of Earth's mass). It is home to 52,910,390 Plutonians."

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)
# Pluto's a planet.
# No, it's a dwarf planet.
# planet!
# dwarf planet!
