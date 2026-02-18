# __Challenge__

# Write a code to calculate multiplication of two random float numbers.

# __Note__
# First random float number must be between 0.1 and 1
# Second random float number must be between 9.5 and 99.5

import random

multiplication = random.random() * random.uniform(9.5, 99.5)

print(f"Multiplication of random numbers: {multiplication}")