# __Challenge__

# Given two strings, s1 and s2, write a program to
# return a new string made of s1 and s2’s first,
# middle, and last characters.

given_string1 = input("Enter 1st string: ")
given_string2 = input("Enter 2nt string: ")

first = given_string1[0] + given_string2[0]

middle = given_string1[len(given_string1)//2] + given_string2[len(given_string2)//2]

last = given_string1[-1] + given_string2[-1]

result = first + middle + last

print(f"New string is: {result}")