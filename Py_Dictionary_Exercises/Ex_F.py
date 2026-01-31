# __Challenge__

# Given a string, create a dictionary where keys are
# characters and values are their frequencies in the
# string.

string1 = 'Manan'

res = dict()

# __Method One__
# for i in string1:
#     res[i] = string1.count(i)

# print(f"Result {res}")

# __Method Two__
for char in string1:
    res[char] = res.get(char,0) + 1

print(res)