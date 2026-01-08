# __Challenge__

# Print pattern.
import math

numberOfRows = int(input("Enter the number of rows in odd: "))

if numberOfRows % 2 == 0:
    print("Only odd number of rows are allowed!")
else:
    for row in range(1, math.ceil(numberOfRows / 2)):
        for col in range(1, row + 1):
            print("*", end=" ")
        print()

    for row in range(math.ceil(numberOfRows / 2), 0, -1):
        for col in range(row, 0, -1):
            print("*", end=" ")
        print()

