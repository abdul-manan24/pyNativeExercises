# __Challenge__

# Write a code to create a Python set such that it
# shows the element from both lists in a pair.

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = set()

for numbers in zip(first_list, second_list):
    result.add(numbers)

print(result)

# another method.

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)