# __Challenge__

# Write a function to flatten a list of lists into a single,
# non-nested list. (e.g., [[1, 2], [3, 4]] becomes [1, 2, 3, 4]).

list_of_lists = [[1, 2], 6, [3, 4], [5, 6, 7]]

flate_list = []

for i in list_of_lists:
    if isinstance(i,list):
        for j in i:
            flate_list.append(j)
    else: 
        flate_list.append(i)

print(f"Original list: {list_of_lists}")
print(f"Flate list: {flate_list}")