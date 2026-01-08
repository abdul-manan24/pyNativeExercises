# __Challenge__

# Write a Python program to print the reverse number pattern using a for loop.

numberOfRows = int(input("Enter number of rows: "))

for row in range(numberOfRows, 0, -1):
    for col in range(row, 0, -1):
        print(col, end=" ")
    print()