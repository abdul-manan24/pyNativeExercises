# __Challenge__

# Write a code to merge two dictionaries into a new dictionary and print it.

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# __Method One__
# dict3 = dict1 | dict2
# print(dict3)

# __Method Two__
# dict1.update(dict2)
# print(dict1)

# __Method Three__
merged_dict = {**dict1, **dict2}
print(merged_dict)