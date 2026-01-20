# __Challenge__

# Write a program to iterate a given list and check
# if a given element exists as a key’s value in a
# dictionary. If not, delete it from the list.

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

new_rollNo = [item for item in roll_number if item in sample_dict.values()]

for num in roll_number:
    if num not in sample_dict.values():
        roll_number.remove(num)

print(roll_number)
print(new_rollNo)

# This algorithm need further research and thinking.