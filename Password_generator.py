import random
import string

print("🔐 Welcome to the Advanced Password Generator 🔐")

# Ask user for password length
while True:
    try:
        length = int(input("Enter password length (e.g. 12): "))
        if length < 4:
            print("Please enter a length of at least 4.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Ask user what to include
include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Build the character pool
characters = list(string.ascii_lowercase)

if include_upper:
    characters += list(string.ascii_uppercase)
if include_numbers:
    characters += list(string.digits)
if include_symbols:
    characters += list(string.punctuation)

# Make sure the pool is not empty
if not characters:
    print("You must select at least one character set!")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\n✅ Your generated password:")
    print(password)
  Initial commit of password generator script
