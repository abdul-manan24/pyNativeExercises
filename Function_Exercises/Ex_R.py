# __Challenge__

# Create Higher-Order Function.

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def apply_operation(func,x,y):
    return func(x,y)

print(apply_operation(addition, 7, 8))
print(apply_operation(subtraction, 7, 8))