# __Challenge__

# Find all occurrences of a substring in a given string by ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?"
country = "USA"

count = str1.lower().count(country.lower())

print(f"Count is {count}")