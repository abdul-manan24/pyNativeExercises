# __Challenge__

# Write a program to iterate a given list and count
# the occurrence of each element and create a dictionary
# to show the count of each element.

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

result = dict()

count = 1

for number in range(0, len(sample_list)):
    if sample_list[number] in result:
        continue
    for number2 in range(number + 1, len(sample_list)):
        if sample_list[number] == sample_list[number2]:
            count += 1
    
    result.update({sample_list[number]:count})
    count = 1

print(result)