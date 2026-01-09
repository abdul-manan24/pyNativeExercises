# __Challenge__

# Write a program to check if the given file is empty or not.

import os

file_size = os.stat(r"E:\pyNative\Input_Output_Exercises\Ex_VI\newFile.txt").st_size

print(f"File size is {file_size}")