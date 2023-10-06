"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
x = float(input("Enter a number: "))
y = float(input("Enter a second number: "))
n = input("Is one of the numbers the hypotenuse of a right triangle? ")
if n == "Yes":
    
    print(f"The length of the missing side is {round(math.sqrt(pow(max(x, y), 2) - pow(min(x, y), 2)), 1)}.")