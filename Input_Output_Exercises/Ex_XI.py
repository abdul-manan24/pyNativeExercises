# __Challenge__

# Ask the user for a numerator and a denominator. Calculate
# the percentage and display it with two decimal places followed
# by a percent sign (e.g., 75.50%).

numerater = float(input("Enter numerater: "))
denominator = float(input("Enter denominator: "))

percentage = "Percentage is: {0:.2f}".format(numerater/denominator * 100)

print(percentage)

