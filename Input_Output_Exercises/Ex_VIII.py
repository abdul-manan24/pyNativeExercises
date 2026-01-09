# __Challenge__

# Write a program to use the string.format() method to format
# the following three variables according to the expected output.

totalMoney = 1000
quantity = 3
price = 450

Statement_1 = "I have {0} so i can buy {1} footballs for {2:.2f}" 

print(Statement_1.format(totalMoney, quantity, price))