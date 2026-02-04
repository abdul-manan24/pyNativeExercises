# __Challenge__

# Write a code to filter out students with scores less than 90 from a given a list of tuples.

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]

students_above_90 = []

for student in students:
    if student[1] >= 90:
        students_above_90.append(student)

print(f"Students above ninety: {students_above_90}")
