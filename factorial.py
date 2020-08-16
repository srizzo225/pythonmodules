#Sara Margaret Rizzo
#2020-08-16
#Problem 6: Use a for statement to calculate the factorial of a user input value. 
#Print this value as well as the calculated value using the factorial function in the math module.

import math
#ask user for value, assign variable x
x = int(input("Enter a number: "))
#assign factorial a value of 1 to start
fact = 1

#for loop to calculate the factorial
for i in range(1, x + 1):
  fact = fact * i
print(x, "factorial is", fact)

#math module function to calculate factorial
print(x, "factorial is", math.factorial(x))