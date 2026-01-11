# __Challenge__

# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

for str in str_list:
    if str == "" or str is None:
        str_list.remove(str)

print(str_list)