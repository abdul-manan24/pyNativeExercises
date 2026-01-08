# __Challenge__

# Capitalize first letter of each word in string.

str = input("Enter an string: ")

result = []

for i in range(len(str)):
    if i == 0 or str[i-1] == ' ':
        result.append(str[i].upper())
    else:
        result.append(str[i])

print(''.join(result))