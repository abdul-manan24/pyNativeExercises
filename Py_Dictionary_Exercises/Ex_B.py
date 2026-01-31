# __Challenge__

# Perform following operations on given dictionary

# Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
# Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
# Check if Key Exists in the dictionary.

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
print(f"Original Dictionary: {my_dict}")

del my_dict["profession"]
print(f"Updated Dictionary: {my_dict}")


for key, value in my_dict.items():
    print(f"{key}: {value}")

ageExists = "profession" in my_dict

print(f"Does age exist? {ageExists}")