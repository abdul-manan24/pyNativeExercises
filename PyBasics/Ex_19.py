# __Challenge__

# Print Alternate Prime Numbers till 20.

target = int(input("Enter range of prime number: "))

def isPrimeNumber(n):
    if n < 2:
        return False
    
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return False
        
    return True

primeNumbers = []

for i in range(target + 1):
    if isPrimeNumber(i):
        primeNumbers.append(i)

for num in range(0, len(primeNumbers), 2):
    print(primeNumbers[num], end=" ")