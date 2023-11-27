# Problem #1

# Loop A
n = 0
while n < 3:
    print(n)
    n = n + 1

# Loop B
i = 0
while i < 3:
    j = 0
    while j < i + 1:
        print("*", end ="")
        j = j + 1
    print("!")
    i = i + 1

# Problem #2


def squares_less_than_n(n):
    if n < 1:
        print("Parameter value must be greater than 0")
    else:
        # Add your code here
        square = 0
        i = 1
        while (i ** 2) <= n:
            square = i ** 2
            print(square)
            i = i + 1


# Verify everything works as intended
value = 50
squares_less_than_n(value) # this should print 1 4 9 16 25 36 49

# Problem #3


def smallest_factor(n):
    if n <1:
        return 0
    else:
        # add your code here
        factor = 2
        while factor <= n:
            if n % factor == 0:
                return factor
        factor = factor + 1


# Verify everything works as intended
number = int(input("Enter a number that is greater than 0: "))
print(smallest_factor(number))


# Problem #4
# Add your code here

def milage_calculator(x, y, z):
    days = 0
    while x <= y:
        x = x + (x * (z/100))
        days = days + 1
    return days


start_milage = float(input("What is the starting milage ran per day?"))
end_milage = float(input("What is the final milage ran to complete the requirement?"))
percent_increase = float(input("What is the percentage increase each day?"))


print(milage_calculator(start_milage, end_milage, percent_increase))


def read_data_file(filename):
    data_file = open(filename, "r")
    header_line = data_file.readline()  # Read the header line of the file to extract years

    years = header_line.strip().split(",")[1:]  # Extract the years from the header line

    # Initialize an empty dictionary to store the data
    data_dict = {}

    # Iterate over each line in the data file
    for line in data_file:

        # Remove leading and trailing whitespaces, and split the line into a list using commas
        line = line.strip().split(",")
        # Create a nested dictionary for each county in the data_dict
        data_dict[line[0]] = {}

        # Iterate over the years and assign the corresponding values to the data_dict
        for i in range(0, len(years)):
            data_dict[line[0]][int(years[i])] = line[i + 1]

    # Close the file
    data_file.close()

    # Return the final data dictionary
    return data_dict


# Uncomment the following line to display the dictionary data structure
# print(read_data_file("coal_production.csv"))

# Add your code here
def calculate_total_production(coal_production_data):
    total_production_by_county = {}

    counties = list(coal_production_data.keys())

    i = 0
    while i < len(counties):
        county = counties[i]
        production_data = coal_production_data[county]
        total_production = 0
        for year in production_data:
            total_production += int(production_data[year])
        total_production_by_county[county] = total_production
        i += 1

    return total_production_by_county


coal_data = read_data_file("coal_production.csv")
total_production_result = calculate_total_production(coal_data)

# Print the result
for key, value in total_production_result.items():
    print("The county", key, "has a total coal production of", value)
