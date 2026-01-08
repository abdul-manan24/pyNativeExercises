# __Challenge__

# Calculate income tax for the given income by adhering to the rules below

# Taxable       Income	        Rate (in %)
# First         $10,000	        0
# Next          $10,000	        10
# The remaining	                20


amount = int(input("Enter amount: "))

first = 10000
next = 10000
remaining = amount - first - next

incomeTaxPayable = (10/100 * next) + (20/100 * remaining)

print(f"Income tax payable is ${incomeTaxPayable}")