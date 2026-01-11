# __Challenge__

# Write a program to count occurrences of all characters within a string.

givenString = input("Enter an string: ").upper()

result = {}

for char in givenString:
    result[char] = givenString.count(char)

print(result)