# __Challenge__

# Print alternate numbers pattern.

rows = int(input("Enter number of rows: "))

num = 1
for i in range(1, rows + 1):
    for j in range(num, num + i):
        print(j, end=" ")
    print()
    num += i