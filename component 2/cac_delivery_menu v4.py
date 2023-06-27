# Menu for the user to choose either the Click & Collect or Delivery option.
# Print statement that asks the user whether they want their order to be for Click & Collect or Delivery.
print ("Do you want your order to be CLICK & COLLECT or DELIVERED to you?")

# Separate Print Statement lines.
print ("For CLICK & COLLECT, enter 1.") # Print statement asking the user to enter d for Delivery.
print ("For DELIVERY, enter 2.") # Print statement asking the user to enter c for Click & Collect.


# The 'while True' loop will create an infinite loop.
while True:
    try: # The try statement will catch and handle except statements.
        # Asking the user to enter their option.
        # The 'int' will make sure what the user inputs is an interger.
        delivery = int(input("Please enter a valid number. ")) # The print statement prints and after this, the user enters their input.

        # The 'and' combines these two conditions. Both conditions must be true for the whole expression to be true.
        # First condition checks if the delivery is an integer that is greater than or equal to 1.
        # Second condition checks if the delivery is an integer that is less than or equal to 2.
        # If both conditions are met, then the program will run either of the if or elif statement.
        # If both or either of the conditions are not met, then the program will skip the if or elif statements and skip to the next part of the code.
        if delivery >= 1 and delivery <= 2:
            if delivery == 1: # Checking if what is entered is '1'.
                print ("Click & Collect") # If '1' is entered, 'Click & Collect' will be printed.
                break # Once the input satisfies this point of the code, the program will break out of this while loop.
        
            elif delivery == 2: # Checking if what is entered is '2'.
                print ("Delivery") # If '2' is entered, 'Delivery' will be printed.
                break # Once the input satisfies this point of the code, the program will break out of this while loop.
        
        # When input is a number that is not 1 or 2, the program will run the else statement.
        else:
            print("The number you enter must be 1 or 2.") # Letting the user know why their input did not work.
    
    # When the user does not enter either '1' or '2', the ValueError will print these error messages.
    except ValueError:
        print("That is not a valid number.")
        print("Please enter 1 or 2.")