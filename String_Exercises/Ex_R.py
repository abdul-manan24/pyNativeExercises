# __Challenge__

# Write a program to find words with both alphabets and numbers from an input string.

str1 = "Emma265 is Data scientist50 and AI Expert"

words = str1.split(" ")

result_words = []

for word in words:
    for char in word:
        if char.isdigit():
            result_words.append(word)
            break

for word in result_words:
    print(word)