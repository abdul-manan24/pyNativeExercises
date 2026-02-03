# __Challenge__

# Change value of a key in a nested dictionary.

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

print(f"Original Dict: {sample_dict}")

sample_dict['emp3']['salary'] = 8500

# for key, value in sample_dict.items():
#     for key2, value2 in value.items():
#         if value2 == 'Brad':
#             value2["salary"] = 8500
#             break

print(f"Modified Dict: {sample_dict}")

# Needs furhter research.