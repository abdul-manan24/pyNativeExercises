# __Challenge__

# Define a global variable global_var = 10. Write a
# function that modifies a global variable value.

global_var = 10

def modifier():
    global global_var
    global_var += 1

modifier()
print(global_var) 