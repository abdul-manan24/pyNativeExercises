# __Challenge__

# Given a list of numbers. write a program to turn every item of a list into its square.

numbers = [1, 2, 3, 4, 5, 6, 7]

squared_list = []

for number in numbers:
    squared_list.append(number ** 2)

print(f"Squared list: {squared_list}")