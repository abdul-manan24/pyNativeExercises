# __Challenge__

# Write a recursive function to calculate the factorial of a non-negative integer.

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(3))