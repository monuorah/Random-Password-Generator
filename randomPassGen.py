import random

print()
print('Welcome to Password Generator\n')

lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = lower_letters.upper()
digits = '0123456789'
symbols = '~!@#$%^&*-+?<>:'
chars = ''  # Will be used to combine characters for user password preference
password = ''
upper, lower, dig, sym = True, True, True, True

length = int(input('Length of password: '))  # Password length
amount = int(input('How many passwords: '))  # Amount of passwords to generate
caps = input('Would you like upper case letters(y or n): ')  # Specify if user wants upper case letters
small = input('Would you like lower case letters(y or n): ')  # Specify if user wants lower case letters
nums = input('Would you like numbers(y or n): ')  # Specify if user wants numbers
signs = input('Would you like symbols(y or n): ')  # Specify if user wants symbols

if caps == 'y':
    upper = True
else:
    upper = False

if small == 'y':
    lower = True
else:
    lower = False

if nums == 'y':
    dig = True
else:
    dig = False

if signs == 'y':
    sym = True
else:
    sym = False

print('\nGenerated Passwords:\n')

if upper and lower and dig and sym:  # If user wants uppercase, lowercase, numbers and symbols
    chars += upper_letters + lower_letters + digits + symbols
    for i in range(amount):
        password = ''.join(random.sample(chars, length))
        print(password)

if upper and lower and not dig and sym:  # If user wants uppercase, lowercase and symbols
    chars += upper_letters + lower_letters + symbols
    for i in range(amount):
        password = ''.join(random.sample(chars, length))
        print(password)

if not upper and lower and dig and sym:  # If user wants lowercase, numbers and symbols
    chars += lower_letters + digits + symbols
    for i in range(amount):
        password = ''.join(random.sample(chars, length))
        print(password)

if upper and lower and dig and not sym:  # If user wants uppercase, lowercase and numbers
    chars += upper_letters + lower_letters + digits
    for i in range(amount):
        password = ''.join(random.sample(chars, length))
        print(password)

if upper and not lower and dig and sym:  # If user wants uppercase, numbers and symbols
    chars += upper_letters + digits + symbols
    for i in range(amount):
        password = ''.join(random.sample(chars, length))
        print(password)
