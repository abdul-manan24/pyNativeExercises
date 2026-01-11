# __Challenge__

# Create a string made of the first, middle and last character.

given_string = input("Enter any string: ")

new_string = given_string[0] + given_string[len(given_string)//2] + given_string[-1]

print(f"Given string: {given_string:} New string: {new_string}")