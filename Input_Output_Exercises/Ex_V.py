# __Challenge__

# Accept a list of 5 float numbers as an input from the user.

def listInput(Datatype):
    givenList = []

    while (True):
        Element = Datatype(input("Enter element of list: "))
        givenList.append(Element)
        userChoice = input("Do you want to continue? (Yes/No): ")
        if userChoice.upper() == "NO":
            break
    
    return givenList

list = listInput(float)

print(list)