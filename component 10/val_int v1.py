# MENU FOR CLICK & COLLECT/DELIVERY. ~~~~~~~~~~~~~~
# Menu for the user to choose either the Click & Collect or Delivery option.
# The function is asking the user for a number.
def order_type():
    # The 'while True' loop will create an infinite loop.
    while True:
        try: # The try statement will catch and handle except statements. Trying to get input from the user.
            # Asking the user to enter their option.
            # The 'int' will make sure what the user inputs is an interger.
            num = int(input()) # The print statement prints and after this, the user enters their input. Trying to get an integer.

            # The 'and' combines these two conditions. Both conditions must be true for the whole expression to be true.
            # First condition checks if the num is an integer that is greater than or equal to 1.
            # Second condition checks if the num is an integer that is less than or equal to 2.
            # If both conditions are met, then the program will run either of the if or elif statement.
            # If both or either of the conditions are not met, then the program will skip the if or elif statements and skip to the next part of the code.
            if num >= 1 and num <= 2:
                # Storing 1 or 2 into the variable, 'answer'.
                return num # Return means that this number, 1 or 2, is stored into the variable, answer. Breaks out of loop.
            # When input is a number that is not 1 or 2, the program will run the else statement.
            else:
                print("The number you enter must be 1 or 2.") # Letting the user know why their input did not work.
        
        # When the user does not enter either '1' or '2', the ValueError will print these error messages.
        except ValueError:
            print("That is not a valid number.")
            print("Please enter 1 or 2.")


# Asking the user to enter a number between 1 or 2 for testing.
print("Enter a number between 1 and 2. ")


# The variable, 'answer', will equal to what comes out of the function, 'order_type'.
answer = order_type() # The variable, answer, is equal to whatever it got from the function, order_type.


# Printing the variable for testing.
print(answer)