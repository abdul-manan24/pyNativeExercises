# __Challenge__

# Given two lists of numbers, write Python code to create
# a new list containing odd numbers from the first list
# and even numbers from the second list.

List_1 = [10, 20, 25, 31, 35]
List_2 = [40, 45, 60, 75, 91]

resultList = []

# Filtering odd numbers from List_1.
for num in List_1:
    if num % 2 == 1:
        resultList.append(num)

# Filtering even numbers from List_2
for num in List_2:
    if num % 2 == 0:
        resultList.append(num)

print(resultList)

