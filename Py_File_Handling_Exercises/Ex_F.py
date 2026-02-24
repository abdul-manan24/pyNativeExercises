# __Challenge__

# Write a program to count the occurrences of a specific word (e.g., “hello”) in a given file.

def count_occurrence_of_word(filename, word):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            count = content.count(word)
            return count
    except:
        f"Error '{filename}' not found!"

# example usage.

count = count_occurrence_of_word('E:\pyNative\Py_File_Handling_Exercises\sample.txt',"line")
print(f"Word 'Line' occurred {count} times in file.")