# __Challenge__

# Write a program to rename a key city to a location in the following dictionary.

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

print(f"Original dictionary: {sample_dict}")

sample_dict['Location'] = sample_dict.pop('city')

print(f"New dictionary: {sample_dict}")