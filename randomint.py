#Sara Margaret Rizzo
#2020-08-16

#Problem 2: Use random.randrange to print an odd integer between 0 and 100.

import random
#0 and 100 are even numbers so they can be excluded from the range.
#if we start at 1, every other number is odd
print(random.randrange(1,100,2))

