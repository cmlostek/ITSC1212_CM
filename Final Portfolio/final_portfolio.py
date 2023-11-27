with open("CoromonDataset.csv", 'r') as f:
    data = f.readlines()

headers = data[0].strip().split(',')
data_types = [line.strip().split(',') for line in data[1:]]

coromon = []
for i in data_types:
    coromon.append(i)
# print(coromon)

types = []
for _ in coromon:
    if _[1] not in types:
        types.append(_[1])
print("The types of coromon are:", types)


def total_coromon():
    total = len(coromon)
    return total


def random_coromon():
    import random
    r_coromon = random.choice(coromon)
    print("The random coromon is:", r_coromon[0], "and it's type is:", r_coromon[1], "and its Health is:", r_coromon[2], "and its Attack is:", r_coromon[3], "and its Defense is:", r_coromon[4], "and its Special Attack is:", r_coromon[5], "and its Special Defense is:", r_coromon[6], "and its Speed is:", r_coromon[7], "and its Stamina is:", r_coromon[8])


def calculate_avg_stats(coromon_type, coromon_data):
    coromon_list = []
    for data in coromon_data:
        if data[1] == coromon_type:
            coromon_list.append(data)
    if not coromon_list:
        return

    coromon_type_dict = {}
    health = sum(int(data[2]) for data in coromon_list)
    avg_health = health / len(coromon_list)
    coromon_type_dict['health'] = int(avg_health)

    attack = sum(int(data[3]) for data in coromon_list)
    avg_attack = attack / len(coromon_list)
    coromon_type_dict['attack'] = int(avg_attack)

    defense = sum(int(data[4]) for data in coromon_list)
    avg_defense = defense / len(coromon_list)
    coromon_type_dict['defense'] = int(avg_defense)

    special_attack = sum(int(data[5]) for data in coromon_list)
    avg_special_attack = special_attack / len(coromon_list)
    coromon_type_dict['special_attack'] = int(avg_special_attack)

    special_defense = sum(int(data[6]) for data in coromon_list)
    avg_special_defense = special_defense / len(coromon_list)
    coromon_type_dict['special_defense'] = int(avg_special_defense)

    speed = sum(int(data[7]) for data in coromon_list)
    avg_speed = speed / len(coromon_list)
    coromon_type_dict['speed'] = int(avg_speed)

    stamina = sum(int(data[8]) for data in coromon_list)
    avg_stamina = stamina / len(coromon_list)
    coromon_type_dict['stamina'] = int(avg_stamina)

    return coromon_type_dict


def avg_health_stats(coromon_type, coromon_data):
    coromon_list_health = []
    for data in coromon_data:
        if data[1] == coromon_type:
            coromon_list_health.append(data)
    if not coromon_list_health:
        return


    avg_health_dict = {}
    health = sum(int(data[2]) for data in coromon_list_health)
    avg_health = health / len(coromon_list_health)
































print("Welcome to the Coromon Database!")
choice = input("Please select an option from the menu below: \n"
        "1: See the total of all the coromon. \n"
        "2: Select a random coromon and display its properties. \n"
        "3: See all of the coromon types. \n"
        "4: Display the coromon with the lowest and highest health stats respectively. \n"
        "5: Display the coromon with the lowest and highest attack stats respectively. \n"
        "6: Display the coromon with the lowest and highest defense stats respectively. \n"
        "7: Display the coromon with the lowest and highest special attack stats respectively. \n"
        "8: Display the coromon with the lowest and highest special defense stats respectively. \n"
        "9: Display the coromon with the lowest and highest speed stats respectively. \n"
        "10. Display the averages for all the stats for every coromon type.\n")
match choice:
    case "1":
        print(total_coromon())
    case "2":
        print(random_coromon())
    case "3":
        print("The types of coromon are:", types)
    case "4":
        type_ = input("Please select a type of coromon from the list above: ")
        print(avg_health_stats(type_, coromon))





