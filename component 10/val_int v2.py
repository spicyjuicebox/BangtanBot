# MENU FOR CLICK & COLLECT/DELIVERY. ~~~~~~~~~~~~~~
# Menu for the user to choose either the Click & Collect or Delivery option.
# The function is asking the user for a number.
def order_type(low, high, question): # Parameter, using three variables in the function, 'order_type()'.
    # The 'low' becomes 1, 'high' becomes 2, 'question' becomes "Please enter a number between 1 and 2. ".
    # The 'while True' loop will create an infinite loop.
    while True:
        try: # The try statement will catch and handle except statements. Trying to get input from the user.
            # Asking the user to enter their option.
            # The 'int' will make sure what the user inputs is an interger.
            # Using the 'question' parameter.
            num = int(input(question)) # The print statement prints and after this, the user enters their input. Trying to get an integer.

            # The 'and' combines these two conditions. Both conditions must be true for the whole expression to be true.
            # First condition checks if the num is an integer that is greater than or equal to 1.
            # Second condition checks if the num is an integer that is less than or equal to 2.
            # If both conditions are met, then the program will run either of the if or elif statement.
            # If both or either of the conditions are not met, then the program will skip the if or elif statements and skip to the next part of the code.
            if num >= low and num <= high: # Using the 'low' and 'high' parameter.
                # Storing 1 or 2 into the variable, 'answer'.
                return num # Return means that this number, 1 or 2, is stored into the variable, answer. Breaks out of loop.
            # When input is a number that is not 1 or 2, the program will run the else statement.
            else:
                print(f"Please enter a number between {low} and {high}. ") # Letting the user know why their input did not work.
        
        # When the user does not enter either '1' or '2', the ValueError will print these error messages.
        except ValueError:
            print("That is not a valid number.")
            print(f"Please enter a number between {low} and {high}. ")


# Setting the variable 'LOW' to 1 and the variable 'HIGH' to 2.
# LOW and HIGH are capitals which means that they are constant.
# When they are constant, they do not change. They are literal.
# Using the 'LOW' parameter.
LOW = 1 # Set to literal 1.
# Using the 'HIGH' parameter.
HIGH = 2 # Set to literal 2.




# Asking the user to enter a number between 1 or 2 for testing.
# A variable called 'question'.
# Using 'f' to format the 'LOW' and 'HIGH' inside the '{}'.
question = (f"Please enter a number between {LOW} and {HIGH}. ")


# The variable, 'answer', will equal to what comes out of the function, 'order_type'.
answer = order_type(LOW, HIGH, question) # The variable, answer, is equal to whatever it got from the function, order_type.
# The 'LOW, HIGH, question' inside of the brackets is a parameter.


# Printing the variable for testing.
print(answer)