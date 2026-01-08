# __Challenge__

# Print the pattern.

n = int(input("Enter number of rows to print: "))

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print("*", end=" ")
    print()