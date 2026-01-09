# __Challenge__

# Write a program to take three names as input from the user
# in a single call to the input() function.

givenNames = input("Enter three names seperated by space: ")

givenNames = givenNames.split(" ")

count = 1
for name in givenNames:
    print(f"Name {count} is {name}")
    count += 1