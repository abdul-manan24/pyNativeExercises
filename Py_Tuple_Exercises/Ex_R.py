# __Challenge__

# Write a code to count the number of occurrences of item 50 from a tuple.

def countOccurrence(iterable, item):
    return iterable.count(item)

tuple1 = (50, 10, 60, 70, 50, 50, 70)
item = 70


print(f"{item} occurred {countOccurrence(tuple1, item)} times in list!")