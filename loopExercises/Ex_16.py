# __Challenge__

# Write a Python program to print the cube of all numbers from 1 to a given number.

givenNumber = int(input("Enter a number: "))

for i in range(1, givenNumber + 1):
    print(f"Current Number is: {i} and the cube is {i ** 3}")