# Bugs.
# Will only work for valid input 'd' and 'c' (include boundaries).
# Invalid input triggers the else statement but program does not ask for input again.


# Menu for the user to choose either the Click & Collect or Delivery option.
# Print statement that asks the user whether they want their order to be for Click & Collect or Delivery.
print ("Do you want your order to be CLICK & COLLECT or DELIVERED to you?")

# Separate Print Statement lines.
print ("For CLICK & COLLECT, enter 1.") # Print statement asking the user to enter d for Delivery.
print ("For DELIVERY, enter 2.") # Print statement asking the user to enter c for Click & Collect.


# Values of '1' and '2' have been assigned to 'low' and 'high'.
low = 1
high = 2

# the 'while True' loop will create an infinite loop.
while True:
    try: # The try statement will catch and handle except statements.
        delivery = int(input("Please enter a valid number.")) # Asking the user to enter their option.

        if delivery == 1: # Checking if what is entered is '1'.
            print("Click & Collect") # If '1' is entered, 'Click & Collect' will be printed.
        
        elif delivery == 2: # Checking if what is entered is '2'.
            print("Delivery") # If '2' is entered, 'Delivery' will be printed.
    
    # When the user does not enter either '1' or '2', the ValueError will print these error messages.
    except ValueError:
        print("That is not a valid number.")
        print("Please enter 1 or 2.")