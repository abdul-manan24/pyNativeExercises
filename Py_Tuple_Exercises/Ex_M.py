# __Challenge__

# Write a code to create a new tuple with only unique elements.

my_tuple = (1, 2, 2, 3, 4, 4, 5)

print(f"Original tuple: {my_tuple}")

new_tuple = set(my_tuple)
print(f"Tuple with unique elements: {tuple(new_tuple)}")