# Creating Password Generator
import random
import string

# Declare lists of Characters, Numbers and Symbols

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

# Crating a password list
password_list = []

# Taking input from user
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Adding random letters to password list
for char in range(nr_letters):
    password_list.append(random.choice(letters))

# Adding random symbols to password list
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Adding random numbers to password list
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffling the password list
random.shuffle(password_list)

# Converting the password list to a string
password = "".join(password_list)

# Displaying the generated password
print(f"Your password is: {password}")