# Challenge

# Print pattern

target = int(input("Enter number: "))

for i in range(1,target + 1):
    for j in range(i):
        print(i, end=" ")

    print()