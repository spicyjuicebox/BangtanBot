# BangtanBot Program

# Bugs - (List bugs here.)
# Known Bugs - (List known bugs here.)


# IMPORT STATEMENTS found here. ~~~~~~~~~~~~~~
import random # Importing the random module. Provides function for generating random numbers and choosing something random from the selection.
from random import randint # Choosing random integer.


# Constants found here.


# LISTS found here. ~~~~~~~~~~~~~~
# LIST OF RANDOM NAMES ~~~~~~~~~~~~~~
# The line below is a list for 'names' with the sequence of strings for each name.
names = ["Jungkook", "Jimin", "V", "J-Hope", "Suga", "RM", "Jin", "Jaehyun", "Felix", "Sunghoon"]


# Dictionary to store information found here.


# Validation.


# WELCOME MESSAGE WITH RANDOMLY GENERATED NAME ~~~~~~~~~~~~~~
# This is a function for the welcome part of the main program.
# This function is made to generate a random name from the 'names' list above, then print out a welcome message.
# The welcome message will incluce the selected, randomly generated name.
def welcome(): # This new function is defined as 'welcome'.
    # Purpose of what this function is for.
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message.
    Parameters: None.
    Returns: None.
    '''
    num = randint(0,9) # 0 is the lower bound, 9 is the upper bound. Generates a random number between 0 and 9.
    name = (names[num]) # Accessing the 'names' list to assign each with a number from 'num'.
    # START PRINTING THE GREETING ~~~~~~~~~~~~~~
    print("2.. 3.. Hello, we are BTS!")
    print("Thank you for choosing...")
    # The \033[95m" + will make the colour of the text in the print code to the colour purple.
    print("\033[95m" + r"""
    _______      ____    ,---.   .--.  .-_'''-. ,---------.    ____    ,---.   .--.         _______       ,-----.  ,---------.  
    \  ____  \  .'  __ `. |    \  |  | '_( )_   \\          \ .'  __ `. |    \  |  |        \  ____  \   .'  .-,  '.\          \ 
    | |    \ | /   '  \  \|  ,  \ |  ||(_ o _)|  '`--.  ,---'/   '  \  \|  ,  \ |  |        | |    \ |  / ,-.|  \ _ \`--.  ,---' 
    | |____/ / |___|  /  ||  |\_ \|  |. (_,_)/___|   |   \   |___|  /  ||  |\_ \|  |        | |____/ / ;  \  '_ /  | :  |   \    
    |   _ _ '.    _.-`   ||  _( )_\  ||  |  .-----.  :_ _:      _.-`   ||  _( )_\  |        |   _ _ '. |  _`,/ \ _/  |  :_ _:    
    |  ( ' )  \.'   _    || (_ o _)  |'  \  '-   .'  (_I_)   .'   _    || (_ o _)  |        |  ( ' )  \: (  '\_/ \   ;  (_I_)    
    | (_{;}_) ||  _( )_  ||  (_,_)\  | \  `-'`   |  (_(=)_)  |  _( )_  ||  (_,_)\  |        | (_{;}_) | \ `"/  \  ) /  (_(=)_)   
    |  (_,_)  /\ (_ o _) /|  |    |  |  \        /   (_I_)   \ (_ o _) /|  |    |  |        |  (_,_)  /  '. \_/``".'    (_I_)    
    /_______.'  '.(_,_).' '--'    '--'   `'-...-'    '---'    '.(_,_).' '--'    '--'        /_______.'     '-----'      '---'    
                                                                                                                                
    """ + "\033[0m") # The line of code, \033[0m" will ensure that the colour will only affect this print statement.
    # If I do not do the code above, then the other print statements underneath BANGTAN BOT will also be of the colour purple.
    print("We are a trusted chat bot that will help you make online orders for BTS merch!")
    print("My name is {}!". format(name)) # The '{}' will be replaced by what we have formatted, 'name', so that it is replaced with a randomly generated name from the list.
    print("I will be here to help you make your online orders!")


# MENU FOR CLICK & COLLECT/DELIVERY ~~~~~~~~~~~~~~
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


# Click & Collect Information.


# Delivery Information.


# BTS Shop Items.


# Choosing the number of items to purhcase.
# Choosing which items to purchase.


# Print order out - including if order is del or pick up and names and price of each pizza - total cost including any delivery charge.


# Ability to cancel the current order or to proceed with a new order.


# Option to create a new order or to exit out of the program.


# MAIN FUNCTION ~~~~~~~~~~~~~~
# The main function will call the other functions (components).
# Defining the main function.
# This is where I am defining the main function of the main program.
# This function is going to be responsible for running the whole program.
# This is where I will be including the 'welcome()' function as I will run this in the main program.
# This function is defined as 'main()'.
def main():
    # Purpose of the main() function.
    '''
    Purpose: To run all functions.
    Parameters: None.
    Returns: None.
    '''
    welcome() # Action being executed (the 'welcome()' function. Called within the 'main()' function.


# Call the main function.
# Since the welcome() function was called within the main() function, then this main() function will
# - execute the welcome() function when called.
main()