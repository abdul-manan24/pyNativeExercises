# __Challenge__

# Write a function that takes a filename as input and returns
# the total number of characters in that file (including
# spaces and newlines).

def characterCounter(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return len(content)
    except:
        return f"Error '{filename}' not found!"
    
# Example usage
character_count = characterCounter(r"E:\pyNative\Py_File_Handling_Exercises\sample.txt")
print(F"Total number of characters in this file is: {character_count}")