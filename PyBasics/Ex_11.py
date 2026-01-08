# __Challenge__

# For example, If the given integer number is 7536, the output
# shall be “6 3 5 7“, with a space separating the digits.

givenNum = int(input("Enter a number: "))

# Printing number in reverse order.

print("Result: ", end="")
while givenNum != 0:
    print( givenNum % 10, end=" ")
    givenNum //= 10