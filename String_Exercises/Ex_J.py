# __Challenge__

# Given a string s1, write a program to return the sum
# and average of the digits that appear in the string,
# ignoring all other characters.

givenString = input("Enter an string: ")

count = 0
sum = 0

for digit in givenString:
    if digit.isdigit():
        count += 1
        sum = sum + int(digit)

if count == 0:
    print("There are no any numbers in string!")
else:
    average = sum / count
    print(f"Sum is {sum}, Average is {average}")