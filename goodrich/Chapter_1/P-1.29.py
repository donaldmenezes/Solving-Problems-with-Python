import itertools

list(itertools.permutations(['c', 'a', 't', 'd', 'o', 't']))

list(itertools.permutations(['c', 'a', 't', 'd', 'o', 't'],2))


## without the intertools module

import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))
