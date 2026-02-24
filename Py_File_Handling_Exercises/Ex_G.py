# __Challenge__

# Write a Python program to create a new file named “output.txt”
# and write the string “Hello, PYnative!” into it.

def write_in_file(filename, text):
    try:
        with open(filename, 'w') as file:
            file.write(text)
    except:
        f"Error '{filename}' not found!"


# Example usage

text_to_write = "Hello, Manan"
write_in_file("E:\pyNative\Py_File_Handling_Exercises\Output.txt", text_to_write)