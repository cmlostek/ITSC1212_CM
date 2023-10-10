# Lab 4

# Problem 1

phrase = input("Input a phrase that is at least 5 characters long.")

# Takes the length of the phrase and prints it
print(len(phrase))

# Indexes the 3rd character of the string and prints that
print(phrase[2])

# Indexes the second to last character of the string and prints that
print(phrase[-2])

# Slices the first 5 characters of the string and prints that
print(phrase[:5])

# Slices all but the last 2 characters and prints that
print(phrase[:-2])

# Problem 2

items = "pencils, pens, paper, erasers, staples, binders"

# Takes the list items and splits it at the commas, then prints the items list as the string supplies.
supplies = items.split(',')
print(supplies)

# Problem 3

fruits_str = "apple - banana - orange - lemon - mango"

# Takes the fruits_str and splits at the ' - ' in the list, then prints the new list
fruits = fruits_str.split(' - ')
print(fruits)

# Problem 4

items = ["raindrops", "roses", "whiskers", "kittens", "kettles", "mittens"]

# Sets the glue portion of the join method. Uses the join method to join each item in the list using the set glue.
glue = ", "
favorite_things = glue.join(items)

# Prints this new joined function as a string.
print(favorite_things)

# Problem 5

names = ['Emma Watson', 'Geraldine Somerville', 'Rupert Grint', 'Devon Murray', 'Tom Felton', 'Daniel Radcliffe',
         'Warwick Davis', 'Stan Lee', 'Mark Williams', 'Adrian Rawlins', 'Kenny Baker', 'David Bradley',
         'Ian McDiarmid', 'Hugo Weaving', 'David Schofield', 'Orlando Bloom', 'Mike Myers', 'Tyrese Gibson',
         'Greg Ellis', 'Kellan Lutz', 'Julie Walters', 'Karl Urban', 'Will Smith', 'Bernard Hill', 'Anna Kendrick',
         'John Ratzenberger', 'Mackenzie Crook', 'Josh Duhamel', 'Bryce Dallas Howard', 'Mickie McGowan', 'Bill Farmer',
         'Robert Hardy', 'Martin Klebba', 'Jack Angel', 'Shia LaBeouf', 'Ken Jeong', 'Debi Derryberry', 'CCH Pounder',
         'Wes Studi', 'Peter Cullen', 'Michelle Rodriguez', 'Billy Burke', 'Bob Bergen', 'Phil Proctor',
         'Elizabeth Reaser', 'Alan Rickman', 'Frank Oz', 'Sherry Lynn', 'Kevin McNally', 'Bonnie Hunt', 'Seth Rogen',
         'Verne Troyer', 'Andy Serkis', 'Eddie Murphy', 'Marton Csokas', 'Clark Gregg', 'Tom Cruise', 'Tom Hanks',
         'Robbie Coltrane', 'Julie Andrews', 'Geraldine James', 'Alan Tudyk', 'Steve Carell', 'Keira Knightley',
         'Leonard Nimoy', 'Gary Oldman', 'Mark Hamill', 'Harrison Ford', 'Cillian Murphy', 'Tim Allen', 'Zoe Saldana',
         'Cameron Diaz', 'Tobey Maguire', 'Jason Isaacs', 'Wayne Knight', 'Hugh Jackman', 'Sam Worthington',
         'Temuera Morrison', 'Jim Cummings', 'Peter Facinelli', 'Julian Glover', 'Brad Garrett', 'Cameron Bright',
         'Christopher Lee', 'Eric Bana', 'Oliver Ford Davies', 'Laz Alonso', 'Maggie Smith', 'Sayed Badreya',
         'Michael Papajohn', 'Richard Griffiths', 'Haley Joel Osment', 'Naomie Harris', 'Bradley Cooper',
         'Jon Favreau', 'Elizabeth Banks', 'Cheri Oteri', 'Gemma Jones', 'Alec Guinness', 'Dwayne Johnson']

# Sets last to the last item in the list, sets second_last to the second to last item in the list using indexing
last = names[-1]
second_last = names[-2]

# Prints last and second_last
print(last)
print(second_last)

# Problem 6

makes = ['Maserati', 'Honda', 'Subaru', 'Fiat', 'Ford', 'Porsche', 'Ford', 'Lotus']

years = ['2004', '1989', '2002', '2016', '2008', '1970', '1926', '2011']

ids = [1231, 1423, 1212, 1331, 1532, 1207, 1145, 1012]

# Accepts the ID number as an input and makes it an integer
id_number = int(input("Please input an ID number for the car."))

# Searches for the input id number and references it to the list ids.
# It then indexes the value in the list and uses that as the reference for the correct Make and Year.
# Then prints the statement starting with the ID, then A [make] made in the year [year].
# If the input given is not within the ID list, prints an invalid ID response.
if id_number in ids:
    car_index = ids.index(id_number)
    print(id_number, ":", "A", makes[car_index], "in the year", years[car_index])
else:
    print("This is not a valid ID number.")
