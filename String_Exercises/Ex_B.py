# __Challenge__

# Write a program to create a new string made of the middle three characters of an input string.

given_string = input("Enter any string: ")

middle = len(given_string)//2

new_string = given_string[middle - 1] + given_string[middle] + given_string[middle + 1]

print(f"Given string: {given_string:} New string: {new_string}")