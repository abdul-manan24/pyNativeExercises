# __Challenge__

# Create a function with keyword arguments.

def studentInfo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:<8}| {value}")

studentInfo(Name="Abdul Manan", Roll_No="2K24/CSE/8",CGPA="2.99")