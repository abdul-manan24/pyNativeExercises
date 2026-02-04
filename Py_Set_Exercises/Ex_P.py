# __Challenge__

# Write a code to count the number of unique words in the given a sentence.

sentence = "Dog is a simple animal dogs is selfless animal"

words = set(sentence.lower().split(' '))

print("Number of unique words:", len(words))