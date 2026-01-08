# __Challenge__

# Count the total number of digits in a number.

number = int(input("Enter a number: "))

count = 0

while number > 0:
    number //= 10
    count += 1

print(f"Digits in number are {count}")