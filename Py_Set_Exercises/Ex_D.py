# __Challenge__

# Find the difference (set1 - set2). Write a code to
# returns a new set containing elements that are
# present in set1 but not in set2.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(f"Difference of set1 and set2: {set1 - set2}")
print(f"Difference of set1 and set2: {set1.difference(set2)}")
print(f"Difference of set2 and set1: {set2 - set1}")
print(f"Difference of set2 and set1: {set2.difference(set1)}")
