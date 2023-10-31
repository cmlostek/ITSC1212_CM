#  Lab 10

# Problem 1

eng2sp = {'one': 'uno'}

# Add your code   below
eng2sp['two'] = 'dos'
print(eng2sp)

# Problem 2

guests = {'Grace Hopper': 2, 'Richard Tapia': 3, 'Timnit Gebru': 1, 'Radia Perlman': 4, 'Ada Lovelace': 2, 'Ruzena Bajcsy': 1}

more_than_1 = []
# Add your code below
for i in guests:
    if guests[i] > 1:
        more_than_1.append(i)
print(more_than_1)

# Problem 3

text = input("Enter text to analyze: ")
# Add your code below
text = text.lower()
letters = {}
for i in text:
    if i not in letters:
        letters[i] = 0
    letters[i] += 1
print(letters)

# Problem 4

word_synonyms = {
    'travel': ['journey', 'go', 'jaunt', 'move_around', 'move', 'locomote', 'change_of_location', 'traveling', 'locomotion', 'trip'],
    'computer': ['data_processor', 'computing_machine', 'information_processing_system', 'calculator', 'electronic_computer', 'estimator', 'figurer', 'computing_device', 'reckoner'],
    'learn': ['hear', 'acquire', 'pick_up', 'teach', 'take', 'check', 'instruct', 'discover', 'read', 'get_a_line', 'study', 'find_out', 'determine', 'ascertain', 'memorize', 'watch', 'see'],
    'excited': ['shake_up', 'emotional', 'activated', 'frantic', 'energize', 'mad', 'charge_up', 'stimulate', 'worked_up', 'stir', 'charge', 'delirious', 'shake', 'agitate', 'wind_up', 'unrestrained']
}

# Add your code below
word = input("What word would you like to search for?")
word = word.lower()
if word in word_synonyms:
    print(word_synonyms[word])


# Problem 5

message_count = {}

# Add your code below
with open("Email_log.txt", "r") as email_log:
    for line in email_log:
        line = line.strip()  # Remove any leading/trailing whitespace
        email_parts = line.split("@")
        if len(email_parts) == 2:  # Ensure the line contains a valid email address
            values = email_parts[1].split(" ")
            domain = values[0]
            count = int(values[1])

            if domain not in message_count:
                message_count[domain] = 0
            message_count[domain] += count

for domain, count in message_count.items():
    print(f"{domain} {count}")
