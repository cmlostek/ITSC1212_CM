#  Opens the file and sorts it into headers and datatypes. Then it sorts the types of coromon into a list.
with open("CoromonDataset.csv", 'r') as f:
    coromonLst = f.readlines()

headers = coromonLst[0].strip().split(',')
data_types = [line.strip().split(',') for line in coromonLst[1:]]
f.close()

coromon_list = []
for i in data_types:
    coromon_list.append(i)
#  print(coromon)

#  Creates a list of the types of coromon.
types = []
for _ in coromon_list:
    if _[1] not in types:
        types.append(_[1])
# print("The types of coromon are:", types)


#  Totals all the existing coromon.
def total_coromon():
    total = len(coromon_list)
    return total


#  Selects a random coromon from the list.
def random_coromon():
    import random
    r_coromon = random.choice(coromon_list)
    return r_coromon


# Calculates the average stats for each type of coromon.
def calculate_avg_stats(coromon_type, coromon_data):
    coromon_list = []
    for coromon in coromon_data:
        if coromon[1] == coromon_type:
            coromon_list.append(coromon)
    if not coromon_list:
        return


#  Calculates the average health for the given type.
    coromon_type_dict = {}
    health = sum(int(coromon[2]) for coromon in coromon_list)
    avg_health = health / len(coromon_list)
    coromon_type_dict['health'] = int(avg_health)

# Calculates the average attack for the given type.
    attack = sum(int(coromon[3]) for coromon in coromon_list)
    avg_attack = attack / len(coromon_list)
    coromon_type_dict['attack'] = int(avg_attack)

# Calculates the average special attack for the given type.
    defense = sum(int(coromon[4]) for coromon in coromon_list)
    avg_defense = defense / len(coromon_list)
    coromon_type_dict['special attack'] = int(avg_defense)

# Calculates the average defense for the given type.
    special_attack = sum(int(coromon[5]) for coromon in coromon_list)
    avg_special_attack = special_attack / len(coromon_list)
    coromon_type_dict['defense'] = int(avg_special_attack)

# Calculates the average special defense for the given type.
    special_defense = sum(int(coromon[6]) for coromon in coromon_list)
    avg_special_defense = special_defense / len(coromon_list)
    coromon_type_dict['special defense'] = int(avg_special_defense)

# Calculates the average speed for the given type.
    speed = sum(int(coromon[7]) for coromon in coromon_list)
    avg_speed = speed / len(coromon_list)
    coromon_type_dict['speed'] = int(avg_speed)

# Calculates the average stamina for the given type.
    stamina = sum(int(coromon[8]) for coromon in coromon_list)
    avg_stamina = stamina / len(coromon_list)
    coromon_type_dict['stamina'] = int(avg_stamina)

    return coromon_type_dict


#  Analyzes the average stats for each type of coromon.
#  Finds the highest and lowest average stat for each type of coromon by comparing the averages across the entirety of the coromon list.
def analyze_avg_stats(types_, coromon, stat_key):
    n = 0
    highest_avg_type = []
    for coromon_type in types_:
        coromon_dict = calculate_avg_stats(coromon_type, coromon)
        # print(coromon_dict)
        for key, value in coromon_dict.items():
            if key == stat_key:
                if value >= n:
                    n = value
    for i in types_:
        coromon_dict = calculate_avg_stats(i, coromon)
        # print(coromon_dict)
        for key, value in coromon_dict.items():
            if key == stat_key:
                if value == n:
                    highest_avg_type.append(i)
                else:
                    continue
    m = 1000
    lowest_avg_type = []
    for coromon_type in types_:
        coromon_dict = calculate_avg_stats(coromon_type, coromon)
        # print(coromon_dict)
        for key, value in coromon_dict.items():
            if key == stat_key:
                if value < m:
                    m = value
    for i in types_:
        coromon_dict = calculate_avg_stats(i, coromon)
        # print(coromon_dict)
        for key, value in coromon_dict.items():
            if key == stat_key:
                if value == m:
                    lowest_avg_type.append(i)
                else:
                    continue
    print(
        f"The coromon type(s) with the highest average {stat_key} is/are: {highest_avg_type} with an average {stat_key} of {n}")
    print(
        f"The coromon type(s) with the lowest average {stat_key} is/are: {lowest_avg_type} with an average {stat_key} of {m}")

# Runs the menu.
# Match - Case allows you to have the user input a value and then run a function based on that value.
# The program will continue to run until the user enters a value that is not in the menu.
# After each function the user is asked if they would like to continue using the program.
# If they enter "y" the program will continue to run, if they enter "n" the program will exit.


print("-----------------------")
print("Welcome to the Coromon Database!")
run = input("Would you like to continue using the Coromon Database? (y/n) \n")
run = run.lower()
while run == "y":
    choice = input("-------------------\nPlease select an option from the menu below: \n"
        "1: See the total of all the coromon. \n"
        "2: Select a random coromon and display its properties. \n"
        "3: See all of the coromon types. \n"
        "4: Display the coromon with the lowest and highest stat value for every stat type. \n"
        "5: Print all of the types of coromon and their average stats. \n"
        "In order to exit the program enter any value. \n"
        "------------------- \n")
    match choice:
        case "1":
            print(f"There are {total_coromon()} coromon in the database.")
        case "2":
            random_coromon_result = random_coromon()
            print(f"The random coromon is: {random_coromon_result[0]} \n Its type is: {random_coromon_result[1]} \n Its Health is: {random_coromon_result[2]} \n Its Attack is {random_coromon_result[3]} \n Its Defense is {random_coromon_result[4]} \n Its Special Attack is {random_coromon_result[5]} \n Its Special Defense is {random_coromon_result[6]} \n Its Speed is {random_coromon_result[7]} \n Its Stamina is {random_coromon_result[8]}")
        case "3":
            print("The types of coromon are:")
            for i in types:
                print(i)
        case "4":
            stat = input("Please select a stat you would like to view: \n"
                         "Health \n"
                         "Attack \n"
                         "Defense \n"
                         "Special Attack \n"
                         "Special Defense \n"
                         "Speed \n"
                         "Stamina \n")
            stat = stat.lower()
            print(analyze_avg_stats(types, coromon_list, stat))
        case "5":
            for coromon_type in types:
                print(f"Average stats for {coromon_type}: ")
                for key, value in calculate_avg_stats(coromon_type, coromon_list).items():
                    print(f"It has a average {key} of: {value}")
        case _:
            print("This is not a valid input, or you wish to stop using the program! Thank you for using the Coromon Database!")
            exit()
    run = input("Would you like to continue using the Coromon Database? (y/n) \n")
    run = run.lower()
print("Thank you for using the Coromon Database!")
