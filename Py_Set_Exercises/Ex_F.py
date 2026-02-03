# __Challenge__

# Given a Python list, write a program to add all of its elements into a given set.

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

print(f"Original set: {sample_set}")

sample_set.update(sample_list)

print(f"Set after adding elements of list: {sample_set}")