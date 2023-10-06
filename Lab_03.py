# Lab 3

# Problem 1

print('Welcome to ITSC 1212!')

# Problem 2

dog_year = int(input("Please provide your dog's age:"))

human_year = dog_year * 7

print("Your dogs age in dog years", dog_year, "is equivalent to,", human_year, "human years.")

# Problem 3

x = float(input('Enter a number:'))

y = float(input('Enter a number:'))

z = (x + y) / 2

print('The average of the two numbers you have entered is:',z)

# Problem 4

num1 = float(input('Enter a number:'))

num2 = float(input('Enter a number:'))

subtotal = (num1 + num2)

print("The sum of the two numbers you have entered is:", subtotal)

# Problem 5

import random

random = random.randrange(0, 1213)

print(random)

# Problem 6

# Imports the math library
import math

# Asks the user to input a real number
x = int(input("Input a real number:"))

# Takes that number and takes the squareroot of it
x_2 = math.sqrt(x)

# Takes the new value of X - X_2 and puts it to the power of 3 to cube it
x_3 = math.pow(x_2,3)

# Takes the new value of X - X_3 and takes it to the nearest whole number using the ceiling function.
x_4 = math.ceil(x_3)

# Prints the final values of X - X_4
print("Your total value is:", x_4)
