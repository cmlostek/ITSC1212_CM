# Lab 2

# Problem 1

# Write a program that accepts three numbers and prints their sum.

# Inputting the 3 numbers and converting each to an integer
input1 = input("Input the first numer:")
num1 = int(input1)
input2 = input("Input the second number:")
num2 = int(input2)
input3 = input("Input the third number:")
num3 = int(input3)

# Calculating the sum of all 3 numbers
num_sum = num1 + num2 + num3

# Printing the sum
print(num_sum)

# Problem 2

# Write a program that accepts an integer value and prints its previous and next numbers separated by a comma.

# Inputting the number
number = input("What number do you want to use?")
integer1 = int(number)

# Getting the previous number
previous = integer1 - 1

# Getting the next number
next_num = integer1 + 1

# Printing the list
print(previous, ",", next_num)

# Problem 3

# Write a program that reads the length of the base and the height of right-angled triangle and prints the area.
# The area of a right angled-triangle is  1/2 x base x height


# Asking for the base and height of the triangle
input_base = input("What is the base of the triangle?")
base = int(input_base)

input_height = input("What is the height of the triangle?")
height = int(input_height)

# Calculating the area of the triangle
area = base * height * .5

# Printing the area of the triangle
print("The area of the triangle is:", area)

# Problem 4

# Write a program that accepts three values that represent
# cost of order, tip percentage, and tax percentage and calculates
# and displays the final purchase cost/price

# Asking for the cost, tip, and tax values.
cost = int(input("What was the cost of the bill?"))
tip = int(input("What was the tip as a percentage?"))
tip_decimal = tip / 100
tax = int(input("What was the tax as a percentage"))
tax_decimal = tax / 100

# Calculating the total price
total_cost = cost + (cost * tip_decimal) + (cost * tax_decimal)

# Printing the total cost
print(total_cost)
