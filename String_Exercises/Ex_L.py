# __Challenge__

# Reverse a given string.

givenString = input("Enter an string: ")

reversed_string = ''.join(reversed(givenString))

print(reversed_string)

# Using another loop method.

for char in range(len(givenString) - 1, -1, -1):
    print(givenString[char], end="")

print()

# Third method of string slicing.

print(givenString[::-1])