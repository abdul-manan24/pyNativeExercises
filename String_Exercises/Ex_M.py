# __Challenge__

# Write a program to find the last position of a substring “Emma” in a given string.

str1 = "Emma is a data scientist who knows Python. Emma works at google."
sub_str = "Emma"

index = str1.rfind(sub_str)

if index == -1:
    print("The sub string does not exist!")
else:
    print(f"Last occurrence of {sub_str} found at index {index}.")