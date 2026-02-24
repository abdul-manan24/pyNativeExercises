# __Challenge__

# Modify the previous program to append the string “This is
# an appended line.” to the end of “output.txt”.

with open("E:\pyNative\Py_File_Handling_Exercises\Output.txt", 'a') as file:
    text = "This is an appended line"
    file.write("\n" + text)