# __Challenge__

# Print multiplication table of a given number.

givenNumber = int(input("Enter a number: "))

for i in range(1, 10 + 1):
    print(f"{givenNumber} x {i} = {givenNumber * i}")