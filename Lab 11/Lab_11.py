# Problem 1

def add(a, b):
    # add your code here
    total = a + b
    return print(total)


# the following statements call the add function.
# when everything works as expected the program will display 7 and 99.
add(1, 6)
add(-1, 100)


# Problem 2

def iseven(num):
    # add your code here
    return num % 2 == 0


# the following statements call the isEven function.
# when everything works as expected the program will display True and False.
print(iseven(56))
print(iseven(1))


# Problem 3
num_even = []


def get_even(num):
    # add your code here
    for i in num:
        if i % 2 == 0 and i not in num_even:
            num_even.append(i)
    return num_even


result = get_even([1,4,5,6,5,4])
print(result)


# Problem 4
# add your code here
min_even = []


def get_min_even(x, y):
    for i in x:
        if i % 2 == 0 and i not in min_even and i > y:
            min_even.append(i)
    return min_even


results = get_min_even([1, 4, 5, 6, 5, 4, 8, 10, 13, 12], 2)
print(results)


# Problem 5
# add your code here
def word_count(word):
    words = word.split(" ")
    count = len(words)
    return count


results = word_count("From a programmer’s point of view the user is a peripheral that types when you issue a read request")
print(results)
