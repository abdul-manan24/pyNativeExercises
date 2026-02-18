# __Challenge__

# Write a code to generate 100 random lottery tickets and pick
# two lucky tickets from it as a winner.
import random

randList = []
count = 0

for number in range(10):
    randList.append(random.randrange(1000000000, 9999999999))

print(f"Start", randList)

print(f"Lucky winner: {random.sample(randList, k=2)}")