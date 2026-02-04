# __Challenge__

# Given a tuple of numbers, create a new tuple where each number is squared.

t = (1, 2, 3, 4)

squared_tuple = tuple(map(lambda x: x*x, t))

print(f"Original tuple: {t}")
print(f"Squared tuple: {squared_tuple}")