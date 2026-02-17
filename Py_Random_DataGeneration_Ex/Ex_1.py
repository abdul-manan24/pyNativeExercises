# __Challenge__

# Write a code to generate 3 random integers between 100 and 999 which is divisible by 5.
import random

randNumbers = []
count = 0

while count<3:
    number = random.randrange(100, 1000)
    if number%5 == 0:
        randNumbers.append(number)
        count +=1

print(randNumbers)

# __Another Method__

print("Random Number:")
for i in range(3):
    print(random.randrange(100, 999, 5), end=", ")
