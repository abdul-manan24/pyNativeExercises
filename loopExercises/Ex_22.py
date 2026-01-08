# __Challenge__
87
# Find largest and smallest digit in a number.
import math

givenNumber = int(input("Enter a number: "))

largestDigit = givenNumber % 10
smallestDigit = givenNumber % 10

originalNumber = abs(givenNumber)

while originalNumber > 0:
    remainder = originalNumber % 10
    if remainder > largestDigit:
        largestDigit = remainder
    if remainder < smallestDigit:
        smallestDigit = remainder
    originalNumber //= 10

print(f"Larget digit in {givenNumber} is {largestDigit}")
print(f"Smallest digit in {givenNumber} is {smallestDigit}")