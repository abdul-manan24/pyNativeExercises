# __Challenge__

# Reverse an integer number.

givenNumber = int(input("Enter a number: "))

# Printing integer in reverse.
while givenNumber > 0:
    print( givenNumber % 10, end="" )
    givenNumber //= 10