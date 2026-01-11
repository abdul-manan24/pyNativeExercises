# __Challenge__

# Arrange string characters such that lowercase letters should come first.

givenString = input("Enter string: ")

newString = []
upperCaseChar = []

for char in givenString:
    if char.islower():
        newString.append(char)
    else:
        upperCaseChar.append(char)

newString = newString + upperCaseChar

newString = ''.join(newString)

print(newString)