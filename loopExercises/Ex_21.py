# __Challenge__

# Write a program to flatten a nested list using loops.

def flatten_list(list):
    newList = []

    for i in list:
        if type(i) == int:
            newList.append(i)
        else:
            for j in i:
                newList.append(j) 

    return newList

nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
nested_list2 = [2, 4, [8, 0, 3], [0, 9, 5, 8], 8]

flattened = flatten_list(nested_list)
flattened2 = flatten_list(nested_list2)
print("Flattened list:", flattened)
print("Flattened list:", flattened2)