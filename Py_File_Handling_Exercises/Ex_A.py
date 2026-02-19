# __Challenge__

# Write a Python program to read the entire contents of a text file
# named “sample.txt” and print it to the console.

with open(r"E:\pyNative\Py_File_Handling_Exercises\sample.txt", 'r') as file:
    print(file.readline())