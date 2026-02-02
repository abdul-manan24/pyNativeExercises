# __Challenge__

# Write a Python program to create a new dictionary by extracting
# the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

result = {}

for i in sample_dict:
    if i in keys:
        result.update({i : sample_dict[i]})

print(f"Result: {result}")

# Improvement needed.