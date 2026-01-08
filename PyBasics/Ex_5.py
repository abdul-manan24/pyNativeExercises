# Challenge

# Write a code to return True if the list’s first and last numbers
# are the same. If the numbers are different, return False.

def Comparison(List):
    if List[0] == List[-1]:
        return True
    else:
        return False
    
numbers_x = [10, 20, 30, 40, 10]

numbers_y = [75, 20, 30, 40, 10]

print("Result is", Comparison(numbers_y))

print("Result is", Comparison(numbers_x))