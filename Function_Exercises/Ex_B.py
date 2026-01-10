# __Challenge__

# Create a function with variable length of arguments.

def namesOfStudents(*names):
    for name in names:
        print(name)

namesOfStudents("Manan","Faraz","Khaliq")
namesOfStudents("Vishal","Kailash","Muttahar")
