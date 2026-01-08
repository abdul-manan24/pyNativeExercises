# __Challenge__

# Write a code to generates a complete multiplication table for numbers 1 through 10.

for i in range(1, 11):
    print(f"Multiplication table of {i} is:", end=" ")
    for j in range(1, 11):
        print(i * j, end=" ")
    print()