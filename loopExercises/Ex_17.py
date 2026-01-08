# __Challenge__

# Write a program to calculate the sum of this series up to n terms.
# For example, if the number is 2 and the number of terms is 5, then
# the series will be 2+22+222+2222+22222=2469

givenNumber = int(input("Enter a number: "))
numberOfTerms = int(input("Enter number of terms: "))

sum = givenNumber
temp = givenNumber

for i in range(1, numberOfTerms):
    sum += temp * 10 + givenNumber
    temp = temp * 10 + givenNumber

print("Sum is: ", sum) 