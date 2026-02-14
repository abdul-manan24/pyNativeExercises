# __Challenge__

# Create student class that takes name and marks of three subjects as
# argument in constructor. then create the method to print the average.

class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.marks1 = sub1
        self.marks2 = sub2
        self.marks3 = sub3
    
    def average(self):
        average = (self.marks1 + self.marks2 + self.marks3) / 3
        return average
    
student_one = Student("Manan", 99, 98, 97)
print(f"Average of {student_one.name}'s marks is {student_one.average()}")

