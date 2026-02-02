# __Challenge__

# Delete a list of keys from a dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to delete
keys = ["name", "salary"]

for i in sample_dict:
    if i in keys:
        sample_dict.pop(i)

print(f"Result: {sample_dict}")

# Improvement needed.