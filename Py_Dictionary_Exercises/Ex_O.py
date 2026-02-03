# __Challenge__

# Write a code to print the key of a minimum value from the following dictionary.

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

# min = min(sample_dict.values())

# for key, value in sample_dict.items():
#     if min == value:
#         print(key)
#         break

print(min(sample_dict, key=sample_dict.get))

# This needs further research.
