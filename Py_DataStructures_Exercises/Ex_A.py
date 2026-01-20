# __Challenge__

# Given two lists, l1 and l2, write a program to create
# a third list l3 by picking an odd-index element from
# the list l1 and even index elements from the list l2.

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []

# Taking odd index numbers from l1.
for index,num in enumerate(l1):
    if index % 2 == 1:
        l3.append(num)

# Taking Even index numbers from l2.
for index,num in enumerate(l2):
    if index % 2 == 0:
        l3.append(num)

print("Printing final third list.")
print(l3)