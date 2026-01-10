# __Challenge__

# Write a program to create a recursive function that
# calculates the sum of numbers from 0 to 10.

def sum(target):
    if target == 0:
        return 0
    else:
        return target + sum(target - 1)

print(sum(4))