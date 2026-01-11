# __Challenge__

# Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the
# characters in the s1 are present in s2. The character’s
# position doesn’t matter.

def areBalanced(string1,string2):
    if len(string1) <= len(string2):
        shorterString, longerString = string1, string2
    else:
        shorterString, longerString = string2, string1
    result = True

    for char in shorterString:
        if char.upper() not in longerString.upper():
            result = False
    
    return result

string1 = input("Enter 1st string: ")
string2 = input("Enter 2nt string: ")

print(areBalanced(string1,string2))