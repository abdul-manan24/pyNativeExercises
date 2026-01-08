# __Challenge__

# Print Reverse Number Pattern.
target = int(input("Enter number of rows: "))

for row in range(target, 0, -1):
    for col in range(1, row + 1):
        print(target-(row-1), end=" ")
    print()