# __Challenge__

# Given two strings, s1 and s2. Write a program to create
# a new string s3 made of the first char of s1, then the
# last char of s2, Next, the second char of s1 and second
# last char of s2, and so on. Any leftover chars go at the
# end of the result.


givenString1 = input("Enter string: ")
givenString2 = input("Enter string: ")

finalString = []
count = len(givenString2) - 1 

for char1 in givenString1:
    finalString.append(char1)
    for char2 in range(len(givenString2) -1, -1, -1):
        if char2 == count:
            finalString.append(givenString2[char2])
            count -= 1
            break

print(''.join(finalString))