# __Challenge__

# Check if All Values are Unique.

dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
dict3 = {}

def areUnique(dict):
    temp = []

    for value in dict.values():
        if value in temp:
            return False
        else:
            temp.append(value)

    return True

print(areUnique(dict1))
print(areUnique(dict2))
print(areUnique(dict3))