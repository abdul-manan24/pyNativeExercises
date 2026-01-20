# __Challenge__

# Write a code to remove duplicates from a list and
# create a tuple and find the minimum and maximum number.

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_list = []

for num in sample_list:
    if num not in unique_list:
        unique_list.append(num)

print(f"Unique list: {unique_list}")

unique_tuple = tuple(unique_list)

print(f"Unique tuple: {unique_tuple}")

max = unique_tuple[0]
min = unique_tuple[0]

for item in unique_tuple:
    if item > max:
        max = item
    elif item < min:
        min = item
        
print(max)
print(min)