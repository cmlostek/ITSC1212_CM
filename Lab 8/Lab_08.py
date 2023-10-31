#  Lab 08

# Problem 1
x_coordinate = []
y_coordinate = []

# Add your code below
with open("xy.txt", "r") as file_name:
    for i in file_name:
        values = i.strip().split(",")
        x_coordinate.append(float(values[0]))
        y_coordinate.append(float(values[1]))
print(x_coordinate)
print(y_coordinate)
print("The length of the x coordinate list is", len(x_coordinate), "and the type of the first element is:", type(x_coordinate[0]))
print("The length of the y coordinate list is", len(y_coordinate), "and the type of the first element is:", type(y_coordinate[0]))

# Problem 2
word1 = "red"
word2 = "scarlet"

red_count = 0
scarlet_count = 0
# Open the "scarlet.txt" file and process it line by line
with open("scarlet.txt", "r") as file_:
    for line in file_:
        # Split the line into words using spaces and punctuation
        words = line.split(" ")

        for word in words:
            if word == word1:
                red_count += 1
            elif word == word2:
                scarlet_count += 1
# Print the word counts
print(f"The word '{word1}' appears {red_count} times in 'The Study in Scarlet'.")
print(f"The word '{word2}' appears {scarlet_count} times in 'The Study in Scarlet'.")

# Problem 3

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

# Add your code below
with open("file_months.txt", "w") as file_months:
    for i in range(len(months)):
        file_months.write(str(months[i]))
        file_months.write("\n")
file_months.close()

# Problem 4
words_list = []

# Open the file and read the CSV
with open("words5000.csv", "r") as words:
    for line in words:
        # Split the line by a comma and convert to lowercase
        words_list.append(line.strip().lower().split(","))
words.close()

word_input = input("What word would you like to search for in the file?")

word_input_low = word_input.lower()

# Check if the word is in the list of words
found = False
for word in words_list[0]:
    if word_input_low == word:
        found = True
        break

if found:
    print("The word", word_input, "is found in the list.")
else:
    print("The word", word_input, "is not found in the file.")