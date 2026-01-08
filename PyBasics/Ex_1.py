# __Challenge__

# Given two integer numbers, write a Python program to return their
# product only if the product is equal to or lower than 1000. Otherwise,
# return their sum.

numOne = int(input("Enter First Num: "))
numTwo = int(input("Enter Second Num: "))

if numOne * numTwo <= 1000:
    print("The result is", numOne * numTwo)
else:
    print("The result is", numOne + numTwo)
