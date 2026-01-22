# __Challenge__

# Create a copy of a list [10, 20, 30] and modify the copy.
# Print both the original and the copied list to demonstrate
# they are independent.

list1 = [10, 20, 30]

list2 = list1[:]

list2[1] = 40

print(f"List1 {list1}")
print(f"List2 {list2}")