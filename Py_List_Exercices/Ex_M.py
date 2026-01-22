# __Challenge__

# Remove all occurrences of a specific item from a list.

list1 = [5, 20, 15, 20, 25, 50, 20]

list1 = list(filter(lambda num: num != 20, list1))

print(f"Result is: {list1}")