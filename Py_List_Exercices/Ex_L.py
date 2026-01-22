# __Challenge__

# Write a function that takes a list with duplicate elements
# and returns a new list with only unique elements.

list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

list_with_duplicates = set(list_with_duplicates)
list_with_duplicates = list(list_with_duplicates)

print(list_with_duplicates)

