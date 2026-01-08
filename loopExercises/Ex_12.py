# __Challenge__

# Display Fibonacci series up to 10 terms.

terms = int(input("Enter number of terms to print: "))

num1 = 0
num2 = 1

result = 0

for i in range(terms):

    print(num1, end=" ")

    result = num1 + num2
    
    num1 = num2
    num2 = result