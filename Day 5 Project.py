#Password Generator Project
from os import sep
import random

random.seed()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level
# Print In order (letters, numbers, symbols) but random characters

password = []

# Generating random characters from each list then appending to the list
for num in range(0, nr_letters):
    random_letter = random.choice(letters)
    password.append(random_letter)

for num in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)
    
for num in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password.append(random_number)
    
# For printing without spaces
unshuffled_password = ""

# Adding each item to the new string
for item in password:
    unshuffled_password += item

print(f"Unshuffled password: {unshuffled_password}")

# Hard level
# Same as above except order is randomized

# Randomizing items from original password
new_password = random.sample(password, len(password))

shuffled_password = ""

# For printing shuffled password without spaces
for item in new_password:
    shuffled_password += item
    
print(f"Shuffled password: {shuffled_password}")
