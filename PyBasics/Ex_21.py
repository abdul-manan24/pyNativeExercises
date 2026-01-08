# __Challenge__

# Check if a user-entered string contains any digits using a for loop.

str = input("Enter an string: ")

isDigitInStr = False

for char in str:
    if '0' <= char <= '9':
        isDigitInStr = True
    
if isDigitInStr == True:
    print("The given string contains atleast one digit!")
else:
    print("The given string does not conatain any digit!")