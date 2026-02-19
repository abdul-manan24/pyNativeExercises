# __Challenge__

# Write a Python program to read the text file named “sample.txt”
# line by line and print each line.

with open(r"E:\pyNative\Py_File_Handling_Exercises\sample.txt", 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line, end="")