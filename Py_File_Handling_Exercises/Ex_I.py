# __Challenge__

# Write a program that takes two filenames as input (source and destination)
# and copies the content of the source file to the destination file.

with open("E:\pyNative\Py_File_Handling_Exercises\sample.txt", "r") as file:
    content = file.read()

with open("E:\pyNative\Py_File_Handling_Exercises\Output.txt", 'w') as file:
    file.write(content)