# __Challenge__

# Remove empty strings from the list of strings.

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

new_list = list(filter(lambda string: string != "", list1))

print(f"New List: {new_list}")