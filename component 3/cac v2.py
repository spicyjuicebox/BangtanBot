# Bug - accepts blank input.


# Print statement letting the user know that they have to enter in their personal details next.
print("Please enter your customer information for your Click and Collect order.")


# Customer Name
# What the user enters in this input line of code will be assigned to the variable, 'name'.
# Assigning the value, 'False', to the variable, 'valid'.
# By assigning it this way, it is indicated that the condition for the valid variable is not satisfied.
# It is used to track the values being entered by the user into the program and will control the flow of the program.
valid = False
# Starting a while loop as long as the condition is 'not valid'.
while not valid:
    # What the user enters in this input line of code will be assigned to the variable, 'name'.
    name = input("Please enter your name. ")
    if name != "": # Checking if the value of 'name' is not empty.
        print (name) # If the condition for 'if name' is not empty, this line will print the value of 'name'.
        # Use break to get out of the loop.
        break
    # When the condition for the 'if' statement is false, the program will skip to the 'else' code.
    else:
        # The 'else' statement will print this line of code.
        print("Sorry, this cannot be blank.") # The program lets the user know that what they enter cannot be blank.
        # No break so it will continue to go into a loop until the user enters the correct input.


# Customer Phone Number
# What the user enters in this input line of code will be assigned to the variable, 'phone'.
# Assigning the value, 'False', to the variable, 'valid'.
# By assigning it this way, it is indicated that the condition for the valid variable is not satisfied.
# It is used to track the values being entered by the user into the program and will control the flow of the program.
valid = False
# Starting a while loop as long as the condition is 'not valid'.
while not valid:
    # What the user enters in this input line of code will be assigned to the variable, 'phone'.
    phone = input("Please enter your phone number. ")
    if phone != "": # Checking if the value of 'phone' is not empty.
        print (phone) # If the condition for 'if phone' is not empty, this line will print the value of 'phone'.
        # Use break to get out of the loop.
        break
    # When the condition for the 'if' statement is false, the program will skip to the 'else' code.
    else:
        # The 'else' statement will print this line of code.
        print("Sorry, this cannot be blank.") # The program lets the user know that what they enter cannot be blank.
        # No break so it will continue to go into a loop until the user enters the correct input.


print(name) # What the user enters for the name input code will be printed here.
print(phone) # What the user enters for the phone input code will be printed here.