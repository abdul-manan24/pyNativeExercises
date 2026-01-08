# __Challenge__

# Print a downward half-pyramid pattern of stars

target = int(input("Enter rows of star: "))

for row in range(target, 0, -1):
    for col in range(1, row + 1):
        print("*", end=" ")

    print() 