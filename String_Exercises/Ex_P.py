# __Challenge__

# Remove special symbols / punctuation from a string.
import string
givenString = input("Enter an string: ")
givenList = list(givenString)

for char in givenList:
    if char.isalpha():
        continue
    elif char.isdigit():
        continue
    elif char == " ":
        continue
    else:
        givenList.remove(char)
    
print(''.join(givenList))

# Applying another method.

newString = givenString.translate(givenString.maketrans('','',string.punctuation))

print("New string is:", newString)