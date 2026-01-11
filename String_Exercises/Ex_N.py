# __Challenge__

# Write a program to split a given string on hyphens and display each substring.

str1 = "Emma-is-a-data-scientist"

sep_strings = str1.split("-")

print("---Each Substring---")
for str in sep_strings:
    print(str)