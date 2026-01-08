# __Challenge__

# Calculate sum of all numbers from 1 to a given number.

givenNumber = int(input("Enter a number: "))

sum = 0

for i in range(1, givenNumber + 1):
    sum += i

print(f"Sum is {sum}")