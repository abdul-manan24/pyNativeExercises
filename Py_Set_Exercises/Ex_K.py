# __Challenge__

# Write a code to check if two sets have any elements in common.
# If yes, display the common elements

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 20, 10, 50}

# __Method One__

# common_elements = set1 & set2

# if len(common_elements) > 0:
#     print("Sets have elements in common!")
#     print(common_elements)
# else:
#     print("Sets doesn't have elements in common")

# __Method Two__

if set1.isdisjoint(set2):
    print("Set does not have common elements!")
else:
    print("Sets have common elements!")
    print(set1.intersection(set2))