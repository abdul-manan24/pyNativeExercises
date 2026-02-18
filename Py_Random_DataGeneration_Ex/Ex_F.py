# __Challenge__

# Write a code to generate a random password which meets the following conditions.
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
import random
import string

def randomPasswordGenerater(password_length):
    allowed_symbols = string.ascii_letters + string.digits + string.punctuation

    password = random.sample(allowed_symbols, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    random.SystemRandom().shuffle(password)
    password = "".join(password)

    return password

print(f"Password is: {randomPasswordGenerater(10)}")