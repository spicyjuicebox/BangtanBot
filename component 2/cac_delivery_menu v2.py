# Bugs.
# Will only work for valid input 'd' and 'c' (include boundaries).
# Invalid input triggers the else statement but program does not ask for input again.


# Menu for the user to choose either the Click & Collect or Delivery option.
# Print statement that asks the user whether they want their order to be for Click & Collect or Delivery.
print ("Do you want your order to be CLICK & COLLECT or DELIVERED to you?")

# Separate Print Statement lines.
print ("For DELIVERY, enter d.") # Print statement asking the user to enter d for Delivery.
print ("For CLICK & COLLECT, enter c.") # Print statement asking the user to enter c for Click & Collect.


# Whatever is entered in the input will be assigned to the variable of 'delivery'.
delivery = input()

if delivery == "d": # Checking if what is entered is 'd'.
    print("Delivery") # If 'd' is entered, 'Delivery' will be printed.

elif delivery == "c": # Checking if what is entered is 'c'.
    print("Click & Collect") # If 'c' is entered, 'Click & Collect' will be printed.

# Setting up else statement code for invalid input.
# If the user does not enter input that is 'd' or 'c', the program will print this error message.
else:
    print ("That was not a valid input.")