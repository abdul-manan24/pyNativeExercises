# __Challenge__

# Write a function called exponent(base, exp) that returns an int
# value of base raises to the power of exp.

def exponent(base, exp):
    if base == 0 or exp <= 0:
        print("Please give base an integer and exp as non-negative integer!")
        return
    
    result = base

    for i in range(1,exp):
        result = result * base

    return result


print(exponent(3,2))
print(exponent(4,2))