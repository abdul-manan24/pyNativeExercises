# __Challenge__

# Ask the user for a number. Print this number
# padded with leading zeros to a width of 5.

number = input("Enter a number: ")

result = number.zfill(5)

print(f"New number is {result}")