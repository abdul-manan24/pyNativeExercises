# __Challenge__

# You have two lists: names = ["Alice", "Bob", "Charlie"]
# and scores = [85, 92, 78]. Print these lists as a simple
# table with columns “Name” and “Score”.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

zipped_elements = zip(names, scores)

print(f"{'Names':<10}{'Scores':<6}")
print("-" * 16)

for name,score in zipped_elements:
    print(f"{name:<10}{score:<6}")