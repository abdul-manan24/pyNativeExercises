# __Challenge__

# list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], find the common elements using sets.

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

set_of_common_elements = set(list1) & set(list2)

print(f"Common elements: {set_of_common_elements}")