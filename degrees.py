#Sara Mararet Rizzo
#2020-08-16
#Problem 5: Search the internet for how to convert radians to degrees. 
#Write a program to compute the conversion given a user input value. 
#Print this value as well as the calculated value using the degrees function in the math module.
import math

#ask user for radians, covert from string to integer, assign variable x
x = (int(input("How many radians? ")))
#convert radians to degrees using formula
print(x * 180 / math.pi) 
#convert using math module function
print(math.degrees(x))