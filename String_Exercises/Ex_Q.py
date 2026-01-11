# __Challenge__

# Removal all characters from a string except integers.

str1 = 'I am 25 years and 10 months old'

list = []

for char in str1:
    if char.isdigit():
        list.append(char)

print(''.join(list))