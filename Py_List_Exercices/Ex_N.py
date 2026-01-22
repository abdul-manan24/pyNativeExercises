# __Challenge__

# Use list comprehension to create a new list containing only the numbers from a given list.


my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6, 9.8]

my_list = [ i for i in my_list if isinstance(i, (int, float))]

print(my_list)