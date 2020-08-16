#Sara Margaret Rizzo
#2020-08-16
#Problem 4: Search on the internet for a way to calculate an approximation for pi. 
#There are many that use simple arithmetic. Write a program to compute the approximation 
#and then print that value as well as the value of math.pi from the math module.

import math

#calculate pi using Gregory-Leibniz Series
pi = 0
for i in range(1, 10000000, 4):
    pi += 4/i
    pi -= 4/(i+2)
print(pi)
#print pi from math module
print(math.pi)

