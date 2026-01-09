# __Challenge__

# Read Line Number 4 from File.

with open(r"E:\pyNative\Input_Output_Exercises\Ex_VI\test.txt",'r') as file:
    count = 1

    while (True):
        if count == 4:
            print(file.readline())
            break
        file.readline()
        count += 1

