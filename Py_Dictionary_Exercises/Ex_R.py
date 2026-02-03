# __Challenge__

# Sort a dictionary by its keys and print the sorted
# dictionary (as an OrderedDict or by converting to
# a list of tuples).

# __Method One__

# my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}

# print(sorted(my_dict.values()))

from collections import OrderedDict

my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
print(f"Original dictionary: {my_dict}")

# Method 1: Create an OrderedDict (maintains insertion order, good for sorted views)
# In Python 3.7+, dicts already preserve insertion order, so this might be redundant
# if you just create a new dict from sorted items.
print("\nSorted by keys (as OrderedDict):")
sorted_by_key_ordered_dict = OrderedDict(sorted(my_dict.items()))
print(sorted_by_key_ordered_dict)

# Method 2: Convert to a list of (key, value) tuples, sorted by key
print("\nSorted by keys (as list of tuples):")
sorted_list_of_tuples = sorted(my_dict.items())
print(sorted_list_of_tuples)

'''Explanation:
my_dict_for_key_sort.items(): Gives us a list of (key, value) tuples.
sorted(...): Sorts this list of tuples. By default, sorted() sorts tuples based on their first element (the key in this case).
OrderedDict(...): Creates an OrderedDict from these sorted tuples. An OrderedDict remembers the order in which items were inserted.
Or sorted(my_dict_for_key_sort.items()): This directly sorts the (key, value) tuples, giving you a list of tuples sorted by keys.
'''