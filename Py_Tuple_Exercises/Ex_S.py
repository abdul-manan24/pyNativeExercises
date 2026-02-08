# __Challenge__

# Check if all items in the tuple are the same.

tuple1 = (45, 45, 45, 45, 89)

def areAllElementsSame(iterable):
    first = iterable[0]

    for item in iterable:
        if item != first:
            return False
    else:
        return True

print("Are all elements same?", areAllElementsSame(tuple1))