# Lab 7 - Transforming Sequences

# Problem 1

awards = ['Emmy', 'Tony', 'Academy', 'Grammy', 'Oscar']
x = input("What award do you want to check for?")
for i in awards:
    if i == x:
        print("Yes that was found in the list at index:", awards.index(i))
    else:
        print("No that was not found in the list")


# Do not modify the lines above

# Problem 2

my_friends = []

# Do not modify the lines above
while True:
    friends = input("Enter the names of your friends, press enter when you have finished the list:")
    if friends == "":
        break
    else:
        my_friends.append(friends)
my_people = my_friends[:]

while True:
    people = input("Enter the names of your family, press enter when you have finished the list:")
    if people == "":
        break
    else:
        my_people.append(people)
print(my_friends)
print(my_people)


# Problem 3

words = ["read", "work", "walk", "watch", "drink", "surf"]

# Do not modify the lines above

words_ing = []
for i in words:
    words_ing.append(i + "ing")
print(words)
print(words_ing)

# Problem 4

numbers = [71, 96, 88, 76, 39, 34, 17, 88, 40, 69, 51, 23, 84, 74, 14, 84, 20, 63, 37]

# Do not modify the lines above
sqrts = []
for i in numbers:
    sqrts.append(i ** .5)
print(numbers)
print(sqrts)

# Problem 5

words2 = ['Work', 'had', 'been', 'piling', 'up', 'lately', '.', 'Work,', 'work,', 'and', 'more',
    'work', 'seemed', 'to', 'be', 'the', 'theme', 'of', 'the', 'day', '.', 'Day',
    'turned', 'into', 'night', ',', 'and', 'work', 'is', 'still', 'piling', 'up', '.']

# Do not modify the lines above

# In lab7_p5.py you are given a list of strings.
# Complete the program, so it combines the strings into one string and then display the new string.

# Problem 6

star_wars = ["Leia", "Han Solo", "Yoda", "Luke", "C3PO", "R2D2"]

# Do not modify the lines above
x = input("What word would you like to delete from the list?")
for i in star_wars:
    del star_wars[star_wars.index(x)]
print(star_wars)

# Problem 7

cats = [8, 6, 8, 4, 9, 34, 7]

dogs = [5, 23, 14, 30, 10, 15, 7]

cats.sort(reverse=True)
dogs.sort(reverse=True)

new_cats = int(input("How many new cats are at the shelter?"))
new_dogs = int(input("How many new dogs are at the shelter?"))

cats.insert(1, new_cats)
dogs.insert(0, new_dogs)

print(cats)
print(dogs)

# Create the list pets which contains the sums of the corresponding values in the 2 lists (cats and dogs)
pets = [cats[i] + dogs[i] for i in range(min(len(cats), len(dogs)))]
print(pets)

total = 0
for i in range(len(pets)):
    total = total + pets[i]
print("The total number of pets is:", total)


# Do not modify the lines above

# Problem 8

my_str = "The daisies are prettier in the early spring"

my_list = [3, 9, -32, 53, 54, 17, 63, 63, 95, -16, 38, -15]

# Do not modify the lines above
pos_list = []
e_count = my_str.count("e")
for i in range(len(my_list)):
    if i > 0:
        pos_list.append(i)
    else:
        continue
pos_average = sum(pos_list) / len(pos_list)
print(e_count)
name_str = input("What is your first name?")
for i in name_str:
    print(i)
# Problem 9

presidents = ["Washington, George, 2/22/1732, 12/14/1799", "Adams, John, 10/30/1735, 7/4/1826",
              "Jefferson, Thomas, 4/13/1743, 7/4/1826", "Madison, James, 3/16/1751, 6/28/1836",
              "Monroe, James, 4/28/1758, 7/4/1831"]

# Do not modify the line above

for i in presidents:
    parts = i.split(', ')
    last_name = parts[0]
    first_name = parts[1]
    dob = parts[2]
    dod = parts[3]
    print("{} {} ({} - {})".format(first_name, last_name, dob, dod))
