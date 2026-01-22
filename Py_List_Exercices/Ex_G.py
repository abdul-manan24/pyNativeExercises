# __Challenge__

# Count and print how many times 'Football' appears in list.

sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis', 'Football', 'Hockey', 'Football', 'Tennis']

count = 0

for sport in sports:
    if sport == 'Football':
        count += 1

print(f"Count is {count}")