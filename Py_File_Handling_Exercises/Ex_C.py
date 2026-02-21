# __Challenge__

# Write a Python program to read only the first 5 lines of “sample.txt”.

with open(r"E:\pyNative\Py_File_Handling_Exercises\sample.txt", 'r') as file:
    count = 1

    while count < 6:
        print(file.readline(), end="")
        count += 1