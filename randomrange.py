# Sara Margaret Rizzo
# 2020-08-16

# Problem 1: Use a for statement and random.randrange to print 10 random integers between 25 and 35.

#open random module
import random

#pick a random number from 25-35 and print it. Do this 10 times
for i in range(10):
    i= random.randrange(25,36)
    print(i)
