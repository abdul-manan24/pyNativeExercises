# __Challenge__

# Count all letters, digits, and special symbols from a given string.

givenString = input("Enter an string: ")

letters = 0
digits = 0
symbols = 0
space = 0

for char in givenString:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        space += 1 
    else:
        symbols += 1

print("---Total Count---")
print(f"{'Name':<10} {'Count':<5}")
print(f"{'Letters':<10} {letters:<5}")
print(f"{'Digits':<10} {digits:<5}")
print(f"{'Symbols':<10} {symbols:<5}")
print(f"{'Space':<10} {space:<5}")