# __Challenge__

# Write all content of a file into a new file by skipping line number 5.


with open(r'E:\pyNative\Input_Output_Exercises\Ex_VI\test.txt', 'r') as file:
    lines = file.readlines()
    
with open(r'E:\pyNative\Input_Output_Exercises\Ex_VI\newFile.txt', 'w') as file:
    count = 0

    for line in lines:
        count += 1
        if count == 5:
            continue
        else:
            file.write(line)
        