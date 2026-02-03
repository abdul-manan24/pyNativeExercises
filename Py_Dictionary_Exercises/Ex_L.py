# __Challenge__

# Delete a list of keys from a dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# __Method One__
# result = {x:sample_dict[x] for x  in sample_dict if x not in keys}
# print(f"Result: {result}")

# __Method Two__
# result = {}
# for i in sample_dict:
#     if i not in keys:
#         result.update({i : sample_dict[i]})
# print(f"Result: {result}")

# __Method Three__
for i in keys:
    sample_dict.pop(i)

print(f"Result: {sample_dict}")