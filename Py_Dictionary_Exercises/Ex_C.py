# __Challenge__

# Write a Python program to convert two Python lists into a
# dictionary where elements from the first list become keys
# and elements from the second list become values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict()

# __Method One__

for key,value in zip(keys, values):
    result[key] = value

print(f"Result {result}")

# __Methond Two__

