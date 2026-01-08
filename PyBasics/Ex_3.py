# __Challenge__

# Write a Python code to accept a string from the user and
# display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

given_str = input("Enter any string: ")

print("Printing only even index characters")


for i in range(0, len(given_str)):
    if i % 2 == 0:
        print(given_str[i])