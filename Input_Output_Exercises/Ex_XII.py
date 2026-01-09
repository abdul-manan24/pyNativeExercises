# __Challenge__

# Create a simple interactive menu with options like
# “1. Say Hello”, “2. Calculate Square”, “3. Exit”.
# Based on the user’s input, perform the corresponding action

while (True):
    print("")
    userInput = int(input("Please choose from the following:\n1. 'Say Hello',\n2. 'Calculate Square',\n3. 'Exit'\nEnter your choice: "))
    if userInput == 3:
        break
    elif userInput == 2:
        try:
            print("Let's find square")
            givenNum = int(input("Enter a number: "))
            print(f"Square is: {givenNum ** 2}")
        except ValueError:
            print("Invalid type, please enter an integer!")
    elif userInput == 1:
        print("Hello, my friend!")
    else:
        print("Invalid choice, please enter a number between 1-3")