# __Challenge__

# Write Python code to iterate through the first 10
# numbers and, in each iteration, print the sum of the
# current and previous number.

for i in range(10):
    print("Current number", i, "Previous number is", (i-1), "sum is:", (i+(i-1)))