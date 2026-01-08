# __Challene__

# Print all prime numbers within a range.

def isPrimeNumber(n):
    if n < 2:
        return False
    
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return False
        
    return True

start = int(input("Enter starting point of range: "))
end = int (input("Enter ending point of range: "))

print(f"Prime number between {start} and {end} are following:")
for i in range(start, end +1):
    if isPrimeNumber(i):
        print(i)