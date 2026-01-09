# __Challenge__

# Ask the user for a word and a number. Print the word
# right-aligned in a field of width 20, followed by the number.

givenString = input("Enter an string: ")
givenNumber = int(input("Enter a number: "))

formatedString = f"{givenString:>24}{givenNumber}"
print(formatedString)