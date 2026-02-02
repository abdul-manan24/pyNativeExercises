# __Challenge__

# Initialize dictionary with default values.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_Dict = dict.fromkeys(employees,defaults)

print(new_Dict)

print(new_Dict["Kelly"])