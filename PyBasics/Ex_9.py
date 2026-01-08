# __Challenge__

# Write a Python code to check if the given number is a palindrome. A
# palindrome number reads the same forwards and backward. For example,
# 545 is a palindrome number.
import math

given_num = int(input("Enter a number: "))
original_num = given_num
reversed_num = 0

while (given_num != 0 ):
    if given_num < 0:    
        remainder = given_num % -10
        reversed_num = (reversed_num * 10) + remainder
        given_num = math.ceil(given_num / 10)
    else:    
        remainder = given_num % 10
        reversed_num = (reversed_num * 10) + remainder
        given_num //= 10

if original_num == reversed_num:
    print("Given number:", original_num, "Reversed number:", reversed_num, "Ans is", True)
else:
    print("Given number:", original_num, "Reversed number:", reversed_num, "Ans is", False)

# This solution is wrong because negative numbers cannot be palindromes.