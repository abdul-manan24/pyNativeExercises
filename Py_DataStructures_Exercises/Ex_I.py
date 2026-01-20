# __Challenge__

# Extract Unique Dictionary Values to List.

speed = {
    'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52,
    'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54
    }

result = []

for value in speed.values(): 
    if value not in result:
        result.append(value)

print(result)