# __Challenge__

# Write a function calculation() that accepts two variables and
# calculates both their addition and subtraction. The function
# should then return both the sum and the difference in a
# single return statement.

def calculation(a,b):
    sum = a + b
    difference = a - b
    return sum, difference

calculation1 = calculation(8,8)
calculation2 = calculation(9,3)

print(calculation1)
print(calculation2)