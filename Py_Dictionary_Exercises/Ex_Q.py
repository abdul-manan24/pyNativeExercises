# __Challenge__

# Write a code to swap keys and values in a dictionary. Assume all values are unique.

original_dict = {'a': 1, 'b': 2, 'c': 3}

inverted_dict = {original_dict[x]:x for x in original_dict}

print(original_dict)
print(inverted_dict)