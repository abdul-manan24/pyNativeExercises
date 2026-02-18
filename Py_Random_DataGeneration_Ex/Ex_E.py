# __Challenge__

# Write a code to generate random string of length 5.
# Note: String must be the combination of the UPPER case and
# lower case letters only. No numbers and a special symbol.
import random
import string

alphabets = string.ascii_letters

random_string = ''.join(random.choice(alphabets) for _ in range(5))

print(f'Random string: {random_string}')