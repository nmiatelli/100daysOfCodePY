import random

letters = ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'l']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [ '!', '@', '#', '$', '%', '*']

print("Password Generator")
n_letters = int(input("How many letters would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like in your password?\n"))

###Easy level
# password = ""

# for char in range (0, n_letters):
#     password += random.choice(letters)

# for char in range (1, n_numbers + 1):
#     password += random.choice(numbers)

# for char in range (0, n_symbols):
#     password += random.choice(symbols)

# print(password)


###Hard level

password_list = []

for char in range (0, n_letters):
    password_list.append(random.choice(letters))

for char in range (1, n_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range (0, n_symbols):
    password_list.append(random.choice(symbols))


random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your password is {password}")
