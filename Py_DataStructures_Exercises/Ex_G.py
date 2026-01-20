# __Challenge__

# Write a code to checks if one set is a subset or
# superset of another set. If found, delete all
# elements from that set.

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is subset of second?", first_set.issubset(second_set))
print("second set is subset of first?", second_set.issubset(first_set))

print("First set is superset of second?", first_set.issuperset(second_set))
print("Second set is superset of first?", second_set.issuperset(first_set))

first_set.clear()

print(first_set)
print(second_set)