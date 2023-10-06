# Lab 6

# Problem 1

num = int(input("Please give a whole number:"))

if num % 2 == 0:
    print(num, "is an even number!")
else:
    print(num, "is an odd number!")

# Problem 2

num = int(input("Input a number:"))

if num == 0:
    print("0")
elif num > 0:
    print("1")
else:
    print("-1")

# Problem 3

age = int(input("What is your age?"))

if age >= 18:
    print("You can vote!")
elif age > 0 and age < 18:
    print("You cannot vote.")
else:
    print("You are a time traveler!")

# Problem 4

num = int(input("Please input a number 1 - 4:"))

if num == 1:
    print("Wow thats a small number!")
elif num == 2:
    print("Getting there!!")
elif num == 3:
    print("Almost! Just one more to go!")
elif num == 4:
    print("WOOHOO You made it!")
else:
    print("This isnt in the range!")

# Problem 5

psw1 = input("Please input your password!")
psw2 = input("Please confirm your password!")

if psw1 == psw2:
    print("Passwords match, user logged in.")
else:
    print("Passwords do not match, try again.")

# Problem 6

vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
phrase = input("Please input a word or phrase!")

if phrase[0] in vowels:
    print("You entered", phrase, "which starts with a vowel!")
else:
    print("You entered", phrase, "which does not start with a vowel!")

# Problem 7

a = 6
z = 26

for number in range(a, z + 1):
    if number % 2 != 0:
        print(number)

# Problem 8

work_hours = float(input("Enter the number of hours worked this week: "))
hourly_wage = float(input("Enter your hourly rate: "))

if work_hours <= 40:
    paycheck = work_hours * hourly_wage
    print(paycheck)
elif work_hours > 40:
    paycheck = work_hours * (hourly_wage + (hourly_wage * .5))
    print(paycheck)
else:
    print("This is not a valid amount.")

# Problem 9

words = ["apple", "banana", "chocolate", "elephant", "giraffe", "hamburger", "kangaroo", "lemon", "octopus",
         "penguin", "panda", "strawberry", "tiger", "umbrella", "watermelon"]

word = input("Enter a word to search for: ")

if word in words:
    print("Yes,", word, "is in the list!")
else:
    print("No", word, "is not in the list!")

# Problem 10

numbers = [39, 72, 16, 89, 4, 57, 61, 98, 27, 12, 33, 68, 6, 55, 91]

for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i])

print(numbers[::2])

# Problem 11

numbers = [39, 72, 16, 89, 4, 57, 61, 98, 27, 12, 33, 68, 6, 55, 91]
target_number = 4

fsum = 0
for num in numbers:
    if num % target_number == 0:
        fsum += num
print(fsum)

# Problem 12

guest_names = ['Grace Hopper', 'Richard Tapia', 'Timnit Gebru', 'Radia Perlman', 'Ada Lovelace', 'Ruzena Bajcsy']

number_of_guests = [2, 3, 1, 4, 2, 1]

for i in range(len(number_of_guests)):
    if number_of_guests[i] > 1:
        print(guest_names[i])
