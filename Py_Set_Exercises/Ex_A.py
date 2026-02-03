# __Challenge__

# Create a Set: Create a set named fruits containing “apple”, “banana”, “mango”, and “orange”.
# Add Element: Add “grape” to the fruits set.
# Remove Element: Remove “banana” from the fruits set.
# Discard Element: Try to discard “mango” from the fruits set.

fruits = {"apple", "banana", "mango", "orange"}

print(f"After creating set: {fruits}")

fruits.add("grape")

print(F"After adding grape: {fruits}")

fruits.remove("banana")

print(f"After removing banana: {fruits}")

fruits.discard("mango")

print(f"After discarding mango: {fruits}")