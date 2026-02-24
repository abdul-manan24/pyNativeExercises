# __Challenge__

# Create a function that takes a filename as input and returns
# the total number of words in that file.

import re

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            words = re.findall(r'\b\w+\b', content) # Use regex to find whole words
            return len(words)
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

# Example usage:
word_count = count_words(r"E:\pyNative\Py_File_Handling_Exercises\sample.txt")
print(f"Total words in 'sample.txt': {word_count}")