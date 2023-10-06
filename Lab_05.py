# Lab 5

# Problem 1

numbers = ['1', '2', '3', '4']

mult = 1
for n in range(1, 5):
    mult = mult * n
print(mult)  # 24 should be printed

# Problem 2

a = 7
z = 13

nums = range(a, (z+1))
nums = list(nums)
print(nums)

accum = 0
for i in range(a, (z+1)):
    accum = accum + i
print(accum)

# Problem 3

num1 = int(input("What whole number integer would you like to take the factorial of?"))
nums = list(range(1, num1+1))

factor = 1
for n in nums:
    factor = factor * int(n)
print(factor)

# Problem 4

names = ['Grace Hopper', 'Richard Tapia', 'Timnit Gebru', 'Radia Perlman', 'Ada Lovelace', 'Ruzena Bajcsy',
         'Cole Mlostek']

tot = 0
for i in names:
    tot += len(i)
print(tot)

# Problem 5

guest_names = ['Grace Hopper', 'Richard Tapia', 'Timnit Gebru', 'Radia Perlman', 'Ada Lovelace', 'Ruzena Bajcsy']

number_of_guests = [2, 3, 1, 2, 2, 1]

for n in range(len(guest_names)):
    print(guest_names[n], number_of_guests[n])
