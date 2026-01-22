# __Challenge__

# Calculate and print the sum and average of all numbers in a list.

my_list = [10, 20, 30, 40, 50]

sum = 0
count = 0

for num in my_list:
    sum += num
    count += 1

average = sum / count

print(f"Sum is: {sum}")
print(f"Average is: {average}")