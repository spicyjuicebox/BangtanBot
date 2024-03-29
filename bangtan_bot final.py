# BangtanBot Program.

# Known Bugs - (List known bugs here.)
# Bugs - (List bugs here.)
# Bug 03/07/2023: When entering input for 'name', it accepts numbers and other characters ('!') when it should not.
# Bug 03/07/2023: When entering input for 'phone', it accepts letters and other characters ('!') when it should not.


# IMPORT STATEMENTS found here. ~~~~~~~~~~~~~~
# Importing 'sys' is the function class for the 'sys.exit' so that it exits the program.
import sys
# Importing the 'random' module. Provides function for generating random numbers and choosing something random from the selection.
import random
# Importing 'time' will bring the library module, 'time' into the program. This will be used for any time-related functions.
import time
from random import randint  # Choosing random integer.


# CONSTANTS found here. ~~~~~~~~~~~~~~
# These LOW and HIGH constants are now available to every function when brought out of the other functions and up here.
# Setting the variable 'LOW' to 1 and the variable 'HIGH' to 2.
# LOW and HIGH are capitals which means that they are constant.
# When they are constant, they do not change. They are literal.
# Using the 'LOW' parameter.
LOW = 1  # Set to literal 1.
# Using the 'HIGH' parameter.
HIGH = 2  # Set to literal 2.

# The phone numbers in New Zealand are generally 8 to 11 digits long.
# The program should check if the phone number being entered is only ranging and including from 8 to 11 digits long.
# Setting the variables for PH_LOW and PH_HIGH.
# These are parameters. They are used in the function, 'check_phone()'.
PH_LOW = 8  # Lowest amount of digits allowed to be entered.
PH_HIGH = 11  # Highest amount of digits allowed to be entered.


# LISTS found here. ~~~~~~~~~~~~~~
# LIST OF RANDOM NAMES. ~~~~~~~~~~~~~~
# The line below is a list for 'names' with the sequence of strings for each name.
names = ["Jungkook", "Jimin", "V", "J-Hope", "Suga",
         "RM", "Jin", "Jaehyun", "Felix", "Sunghoon"]

# LIST OF ALBUM NAMES. ~~~~~~~~~~~~~~
# This is a list that is named, 'album_names'. This list stores the information of the list of albums that the program will be selling.
# The list is defined using the square brackets, '[]'. Inside these are strings that are separated by commas and are enclosed by single quotes to indicate that each are strings.
# The order of the items in this list will be written out in the same order when printed.
album_names = ['2 Cool 4 Skool', 'O!RUL8,2?', 'Skool Luv Affair', 'No More Dream', 'The Most Beautiful Moment In Life Pt.1', 'The Most Beautiful Moment In Life Pt.2',
               'The Most Beautiful Moment In Life: Young Forever', 'WINGS', 'Love Yourself: Her', 'Love Yourself: Tear', 'Love Yourself: Answer', 'Map of the Soul: Persona', 'Map of the Soul: 7', 'BE', 'Butter']


# LIST OF ALBUM PRICES. ~~~~~~~~~~~~~~
# Another list variable that is named, 'album_prices'.
# The list is defined using the square brackets, '[]'. Inside these are strings that are separated by commas and each represent the price of each of the albums to be sold.
# The order of the prices or numbers in this list will be written out in the same order when printed and aligns itself with the album_names list.
album_prices = [25.70, 32.20, 28.40, 40.20, 40.10, 45.70,
                62.50, 45.80, 50.50, 58.40, 60.80, 52.20, 90.50, 55.50, 40.20]
# The '25.70'lines up with the album_names of '2 Cool 4 Skool' with it being at position 0.

# LIST OF STORED ORDERED ALBUMS. ~~~~~~~~~~~~~~
order_list = []

# LIST OF STORED ALBUM PRICES. ~~~~~~~~~~~~~~
order_cost = []


# DICTIONARY TO STORE INFORMATION found here. ~~~~~~~~~~~~~~
# Customer Details Dictionary.
# Curly brackets indicate a dictionary (stores information - customer details). Holds information, better than a list.
customer_details = {}


# VALIDATION found here. ~~~~~~~~~~~~~~
# Validates Inputs to check if they are blank.
# Function - Everytime you want to check if something is not blank, it is sent to this function. Taking a question/variable from somewhere else.
# This is a parameter. It brings variables ('question') in from different places in our code. Parameter is anything inside the brackets. Bringing in the question.
def not_blank(question):
    # What the user enters in this input line of code will be assigned to the variable, 'name'.
    # Assigning the value, 'False', to the variable, 'valid'.
    # By assigning it this way, it is indicated that the condition for the valid variable is not satisfied.
    # It is used to track the values being entered by the user into the program and will control the flow of the program.
    valid = False
    # Starting a while loop as long as the condition is 'not valid'.
    while not valid:
        # The question is a variable in the input section. It is then brought up as a parameter.
        # Using the variable, 'response'. This is a parameter.
        # The answer to the question will go to the 'response' variable.
        response = input(question)
        if response != "":  # Here, we are going to return the response back out with the function. it is asking for a response and is checking to see if it is blank.
            # Capitalizing the first letter of what is entered.
            # The return will kick out of the loop. It will return it back down and be entered into the dictionary.
            return response.title()
        # When the condition for the 'if' statement is false, the program will skip to the 'else' code.
        else:
            # The 'else' statement will print this line of code (error message).
            print("\n \033[38;2;255;116;116m~! This cannot be blank.\033[0m")


# VALIDATION found here. ~~~~~~~~~~~~~~
# Defining the function, check_string().
# Using the 'isalpha' to check if the input is all alphabetical.
# Bringing in the variable, 'question', into the function.
def check_string(question):
    while True:
        # Using the variable, 'response'. This is a parameter.
        # The answer to the question will go to the 'response' variable.
        response = input(question)
        # Setting up the variable, 'x'.
        x = response.isalpha()
        # The 'isalpha' checks if the string is using the alphabet (alphabetical).
        # Checking if the response is alphabetical or not.
        # Checking if there are numbers or other characters being used in the response.

        # If it is not alphabetical, run the 'if' statement.
        if x == False:
            # Printing the error message.
            print(
                "\n \033[38;2;255;116;116m~! Input must only contain letters.\033[0m\n")
            # Will continue to run the loop until correct input.
        else:
            # The response will be printed and the first letter will be capitalised.
            return (response.title())
# This function will be used whenever a function is asking for a name or for the user's address details (street name and suburb).


# VALIDATION found here. ~~~~~~~~~~~~~~
# Validating the menu for the user to choose either the Click & Collect or Delivery option.
# Validating the inputs to check if they are an integer.
# The function is asking the user for a number.
# Parameter, using three variables in the function, 'order_type()'.
def val_int(low, high, question):
    # The 'low' becomes 1, 'high' becomes 2, 'question' becomes "Please enter a number between 1 and 2. ".
    # The 'while True' loop will create an infinite loop.
    while True:
        try:  # The try statement will catch and handle except statements. Trying to get input from the user.
            # Asking the user to enter their option.
            # The 'int' will make sure what the user's input is an interger.
            # Using the 'question' parameter.
            # Trying the number.
            # The print statement prints and the user enters their input. Trying to get an integer.
            # Their input will be equal to the variable, 'num'.
            num = int(input(question))

            # The 'and' combines these two conditions. Both conditions must be true for the whole expression to be true.
            # First condition checks if the num is an integer that is greater than or equal to 1, low.
            # Second condition checks if the num is an integer that is less than or equal to 2, high.
            # If both conditions are met, then the program will run either of the if or elif statement.
            # If both or either of the conditions are not met, then the program will skip the if or elif statements and skip to the next part of the code.
            if num >= low and num <= high:  # Using the 'low' and 'high' parameter.
                return num
                # Will return the number back to the 'delivery' variable in the 'order_type()' function.
            # When input is a number that is not 1, low, or 2, high, the program will run the else statement (error message).
            else:
                print(
                    f"\n \033[38;2;255;116;116m~! Your number should have been between {low} and {high}.\033[0m\n")
                # This lets the user know why their input did not work.

        # When the user does not enter either '1' or '2', the ValueError will print these error messages.
        except ValueError:
            print(
                "\n \033[38;2;255;116;116m~! That is not a valid number.\033[0m")
            print(
                f"\n \033[38;2;255;116;116m~! Your number should have been between {low} and {high}.\033[0m\n")


# VALIDATION found here. ~~~~~~~~~~~~~~
# Validating if the input for the phone number is all integers.
# Defining the function, check_phone().
# This function will be using parameters.
def check_phone(PH_LOW, PH_HIGH, question):
    # Bringing in the variable, 'question', into the function.
    # Bringing in the variable, 'PH_LOW', for 8, into the function.
    # Bringing in the variable, 'PH_HIGH', for 11, into the function.
    # Starting a while loop.
    while True:
        try:  # Trying if the input is an integer.
            # Setting a variable called, 'num' for the phone number input.
            num = int(input(question))  # Bringing in the 'question' variable.
            # The response to the question will be entered into the 'num' variable.
            # Setting a variable called, 'test_num' to test the number input.
            test_num = num
            # The 'count' counts through how many digits are in the input.
            count = 0
            while test_num > 0:
                # Taking the number and dividing the test_num by 10.
                test_num = test_num//10
                count = count + 1  # Adding 1 to the count variable.
            # Setting up the two conditions in the 'if' statement.
            if count >= PH_LOW and count <= PH_HIGH:
                # Returning breaks out of the loop.
                # Made into a string because if not, the first digit being a 0 will be removed after printing.
                return str(num)
                # Leaving it as it is.
            # If the input phone number is not between and including 8 to 11 digits, the error message will print.
            else:
                print(
                    "\n \033[38;2;255;116;116m~! NZ phone numbers must be 8 to 11 digits long.\033[0m")
        # If the input phone number does not contain all numbers, the error message will print.
        except ValueError:
            print(
                "\n \033[38;2;255;116;116m~! Please enter your phone number using only numbers.\033[0m")
            # Should go into a loop until valid input is entered.


# WELCOME MESSAGE WITH RANDOMLY GENERATED NAME. ~~~~~~~~~~~~~~
# This is a function for the welcome part of the main program.
# This function is made to generate a random name from the 'names' list above, then print out a welcome message.
# The welcome message will incluce the selected, randomly generated name.
# Defining the function, 'welcome()'.
def welcome():  # This new function is defined as 'welcome'.
    # Purpose of what this function is for.
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message.
    Parameters: None.
    Returns: None.
    '''

    # LOADING PROGRESS. ~~~~~~~~~~~~~~
    # This section is using the time module that we have imported.
    # Starting a while loop.
    while True:
        # The 'for' loop is used to iterate over a sequence of 4 elements using the 'range(4)' function, generating sequence between, and including, 0 to 3.
        # The 'i' takes in the variables of 0, 1, 2 and 3.
        # The loop will go through 4 times. Once the process is done, it will break out of the loop.
        for i in range(4):
            # Setting the suffix for the dots to appear.
            # When i = 0, so the string is empty (no '.' will appear).
            # When i = 1, the suffix is set to '.' ('.' will appear).
            # When i = 2, the suffix is set to '..' ('..' will appear).
            # When i = 3, the suffix is set to '...' ('...' will appear). This will be the end of the sequence.
            suffix = '.' * i if i < 3 else '...'
            # The program will print "Loading Program" first and depending on the value of i, the program will print the number of dots after the message.
            print("Loading Program" + suffix, end='\r', flush=True)
            # Each '.' will appear after each second due to the '(1)'.
            time.sleep(1)
        # Breaks out of the while loop so that the rest of the program can continue.
        break

    # 0 is the lower bound, 9 is the upper bound. Generates a random number between 0 and 9.
    num = randint(0, 9)
    # Accessing the 'names' list to assign each with a number from 'num'.
    name = (names[num])

    # START PRINTING THE GREETING. ~~~~~~~~~~~~~~
    print("\033[38;2;215;187;245m\033[1m\"2.. 3.. Hello, we are BTS!\"\033[0m")
    print("\nThank you for choosing...")
    # The '38' indicates to the program that the text is going to change colour.
    # The '2' indicates to the program that a custom RGB colour will be used.
    # The '176;120;249' are the same values of the hex code, #B078F9.
    # The '215;187;245' are the same values of the hex code, #D7BBF5.
    # Used an ascii generator to generate this customized text.
    print("\033[38;2;176;120;249m" + r"""
    _______      ____    ,---.   .--.  .-_'''-. ,---------.    ____    ,---.   .--.         _______       ,-----.  ,---------.  
    \  ____  \  .'  __ `. |    \  |  | '_( )_   \\          \ .'  __ `. |    \  |  |        \  ____  \   .'  .-,  '.\          \ 
    | |    \ | /   '  \  \|  ,  \ |  ||(_ o _)|  '`--.  ,---'/   '  \  \|  ,  \ |  |        | |    \ |  / ,-.|  \ _ \`--.  ,---' 
    | |____/ / |___|  /  ||  |\_ \|  |. (_,_)/___|   |   \   |___|  /  ||  |\_ \|  |        | |____/ / ;  \  '_ /  | :  |   \    
    |   _ _ '.    _.-`   ||  _( )_\  ||  |  .-----.  :_ _:      _.-`   ||  _( )_\  |        |   _ _ '. |  _`,/ \ _/  |  :_ _:    
    |  ( ' )  \.'   _    || (_ o _)  |'  \  '-   .'  (_I_)   .'   _    || (_ o _)  |        |  ( ' )  \: (  '\_/ \   ;  (_I_)    
    | (_{;}_) ||  _( )_  ||  (_,_)\  | \  `-'`   |  (_(=)_)  |  _( )_  ||  (_,_)\  |        | (_{;}_) | \ `"/  \  ) /  (_(=)_)   
    |  (_,_)  /\ (_ o _) /|  |    |  |  \        /   (_I_)   \ (_ o _) /|  |    |  |        |  (_,_)  /  '. \_/``".'    (_I_)    
    /_______.'  '.(_,_).' '--'    '--'   `'-...-'    '---'    '.(_,_).' '--'    '--'        /_______.'     '-----'      '---'    
                                                                                                                                
    """ + "\033[0m")  # The line of code, \033[0m" will ensure that the colour will only affect this print statement.
    # If I do not do the code above, then the other print statements underneath BANGTAN BOT will also be of the colour purple.
    print("We are a trusted program that will help you make online orders for BTS albums!")
    # The '{}' will be replaced by what we have formatted, 'name', so that it is replaced with a randomly generated name from the list.
    print(" ~❀ My name is {}!". format(name))
    print(" ~❀ I will be here to help you make your online orders!\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")


# MENU FOR CLICK & COLLECT/DELIVERY. ~~~~~~~~~~~~~~
# Menu for the user to choose either the Click & Collect or Delivery option.
def order_type():
    del_click = ""  # This variable is equal to default, empty, blank string.
    # This variable will change to 'clickandcollect' if 1 is entered.
    # This variable will change to 'delivery' if 2 is entered.

    # Asking the user to enter a number between 1 or 2.
    # A variable called 'question'.
    # Using 'f' to format the 'LOW' and 'HIGH' inside the '{}'.
    question = (
        f"~ Please enter a number between {LOW} and {HIGH}.\n    Enter: ")

    # Print statement that asks the user whether they want their order to be for Click & Collect or Delivery.
    print(
        "Do you want your order to be \033[38;2;176;120;249m\033[1mCLICK & COLLECT\033[0m or \033[38;2;215;187;245m\033[1mDELIVERED\033[0m to you?\n")
    print(
        "Please note that for delivery orders, a $9.00 delivery charge will be added for 4 or less albums being ordered. Thank you!\n")

    # Separate Print Statement lines.
    # Print statement asking the user to enter 1 for Click & Collect.
    print(
        "    ❀ For \033[38;2;176;120;249m\033[1mCLICK & COLLECT\033[0m, enter \033[38;2;176;120;249m\033[1m1\033[0m.")
    # Print statement asking the user to enter 2 for Delivery.
    print(
        "    ❀ For \033[38;2;215;187;245m\033[1mDELIVERY\033[0m, enter \033[38;2;215;187;245m\033[1m2\033[0m.\n")
    # Asking the user to enter their option.
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:  # Checking if what is entered is '1'.
        # If '1' is entered, 'Click & Collect' will be printed.
        print(
            "    \033[1mYour Order Will Be For:\033[0m \033[38;2;176;120;249mClick and Collect\033[0m")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")
        # If Click & Collect is chosen, then the variable, 'del_click', will equal to "clickandcollect".
        # This will change the 'del_click' variable.
        del_click = "clickandcollect"
        clickandcollect_info()  # Will run the clickandcollect() function.
    # Only other valid option will be 2.
    else:
        # If '2' is entered, 'Delivery' will be printed.
        print(
            "    \033[1mYour Order Will Be For: \033[38;2;215;187;245mDelivery\033[0m")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")
        # If Delivery is chosen, then the variable, 'del_click', will equal to "delivery".
        delivery_info()  # Will run the delivery() function.
        del_click = "delivery"  # This will change the 'del_click' variable.
    # This will return the 'del_click' variable back down to the main() function at 'del_click = order_type()'.
    return del_click


# CLICK & COLLECT INFORMATION. ~~~~~~~~~~~~~~
# Question (variable) comes from here.
# Defining the function, 'clickandcollect()' for the click and collect component of the main program.
def clickandcollect_info():
    # Displaying our question (name).
    question = ("~ Please enter your name (no spaces, please).\n    Enter: ")
    # This will go into the customer_details dictionary and it will have a variable name of 'name'.
    # Getting the customer details 'name' from the above function, bringing in the question.
    # Customer name will go to the function for 'check_string(question)' to check if the input is all alphabetical.
    customer_details['name'] = check_string(question)
    print("    \033[1mYour Name Is:\033[0m {}." .format(
        customer_details['name']))

    # Displaying our question (phone number).
    question = (
        "\n~ Please enter your phone number (no spaces, please).\n    Enter: ")
    # This will go into the customer_details dictionary and it will have a variable name of 'phone'.
    # Getting the customer details 'phone' from the above function, bringing in the question.
    # Customer phone number will go to the function for 'check_phone(PH_LOW, PH_HIGH, question)' to check if the input is all numbers.
    customer_details['phone'] = check_phone(PH_LOW, PH_HIGH, question)
    print("    \033[1mYour Phone Number Is:\033[0m {}." .format(
        customer_details['phone']))
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")


# DELIVERY INFORMATION. ~~~~~~~~~~~~~~
# Question (variable) comes from here.
# Defining the function, 'delivery' for the delivery component of the main program.
def delivery_info():
    # Basic Instructions.
    # Question (variable) comes from here.
    # Displaying our question (name).
    question = ("~ Please enter your name (no spaces, please).\n    Enter: ")
    # This will go into the customer_details dictionary and it will have a variable name of 'name'.
    # Getting the customer details 'name' from the above function, bringing in the question.
    # Customer name will go to the function for 'check_string(question)' to check if the input is all alphabetical.
    customer_details['name'] = check_string(question)
    print("    \033[1mYour Name Is:\033[0m {}." .format(
        customer_details['name']))

    # Displaying our question (phone).
    question = (
        "\n~ Please enter your phone number (no spaces, please).\n    Enter: ")
    # This will go into the customer_details dictionary and it will have a variable name of 'phone'.
    # Getting the customer details 'phone' from the above function, bringing in the question.
    # Customer phone number will go to the function for 'check_phone(PH_LOW, PH_HIGH, question)' to check if the input is all numbers.
    customer_details['phone'] = check_phone(PH_LOW, PH_HIGH, question)
    print("    \033[1mYour Phone Number Is:\033[0m {}." .format(
        customer_details['phone']))

    # Displaying our question. (house number).
    question = ("\n~ Please enter your house number.\n    Enter: ")
    # This will go into the customer_details dictionary and it will have a variable name of 'house'.
    # Getting the customer details 'house' from the above function, bringing in the question.
    # Customer name will go to the function for 'not_blank' to check if the input is not blank or does not contain any spaces.
    customer_details['house'] = not_blank(question)
    print("    \033[1mYour House Number Is:\033[0m {}.\n" .format(
        customer_details['house']))

    # Displaying our question (street name).
    question = ("~ Please enter your street name.\n    Enter: ")
    # This will go into the customer_details dictionary and it will have a variable name of 'street'.
    # Getting the customer details 'street' from the above function, bringing in the question.
    # Customer name will go to the function for 'check_string(question)' to check if the input is all alphabetical.
    customer_details['street'] = check_string(question)
    print("    \033[1mYour Street Name Is:\033[0m {}.\n" .format(
        customer_details['street']))

    # Displaying our question (suburb).
    question = ("~ Please enter your suburb (no spaces, please).\n    Enter: ")
    # This will go into the customer_details dictionary and it will have a variable name of 'suburb'.
    # Getting the customer details 'suburb' from the above function, bringing in the question.
    # Customer name will go to the function for 'check_string(question)' to check if the input is all alphabetical.
    customer_details['suburb'] = check_string(question)
    print("    \033[1mYour Suburb Is:\033[0m {}." .format(
        customer_details['suburb']))
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")


# BTS ALBUMS. ~~~~~~~~~~~~~~
# Defining the function for the albums as albums().
# This function will be responsible for displaying the album names, album prices and their corresponding index numbers.
def albums():
    # Making a variable (will count through 15 times).
    # This is the total number of albums that the bot will be selling (15).
    number_albums = 15

    # The 'for' statement will create a loop that will start from 0 and will range through to the end of 'number_albums - 1' (from 0 to 14).
    print("\033[1mList of Albums Available:\033[0m\n")
    for count in range(number_albums):  # Taking 0.
        print(" \033[38;2;176;120;249m{})\033[0m  {} \n        \033[38;2;155;240;189m~ Price: ${:.2f}\033[0m\n".format(count+1,
              album_names[count], album_prices[count]))  # Prints out each of the album names and album prices by its integer.
        # The {:.2f} rounds them up into 2 decimal places or 2 floats. The 0 appears now.
        # The count+1 will change the 2 Cool 4 Skool position from 0 to 1.
        # The album_names[count] will retrieve the name of the album at the current index, 'count', from the 'album_names' list.
        # The album_prices[count] will retrieve the price of the album at the current index, 'count', from the 'album_prices' list.
        # The output will be printed out through the format, "{album_number} {album_name} ${album_price}".


# CHOOSING THE NUMBER OF ALBUMS TO PURCHASE. ~~~~~~~~~~~~~~
# Choosing which items to purchase - print each album ordered with cost.
# Defining the function for the ordering of the albums as order_album().
def order_album():
    # Ask for total number of albums for order.
    num_albums = 0  # This variable has the value of 0.

    # Setting the variable 'NUM_LOW' to 1 and the variable 'NUM_HIGH' to 8.
    # NUM_LOW and NUM_HIGH are capitals which means that they are constant.
    # When they are constant, they do not change. They are literal.
    NUM_LOW = 1  # Set to literal 1.
    NUM_HIGH = 8  # Set to literal 8.

    # Setting the variable 'MENU_LOW' to 1 and the variable 'MENU_HIGH' to 15.
    MENU_LOW = 1  # Lowest number of available albums.
    MENU_HIGH = 15  # Highest number of available albums.

    # Asking the user to enter a number between 1 or 8.
    # A variable called 'question'.
    # Using 'f' to format the 'NUM_LOW' and 'NUM_HIGH' inside the '{}'.
    question = (
        f"~ Please enter a number between {NUM_LOW} and {NUM_HIGH}.\n    Enter: ")

    # Asking the user how many albums they want to order.
    print("\nHow many albums do you want to order?")
    # The number of albums entered will go through the 'val_int()' function.
    # 'NUM_LOW' is 1, 'NUM_HIGH" is 8, 'question' is "Please enter a number between 1 and 8. ".
    num_albums = val_int(NUM_LOW, NUM_HIGH, question)
    # Choose album from the album list.
    # Used the 'for' statement to create a loop for the number of items that the user has chosen, found in num_albums.
    # Counting through how many albums have been chosen.
    for item in range(num_albums):
        # Another loop is made with the 'while' statement to ensure that the user can enter their chosen number.
        while num_albums > 0:
            print("\nChoose the album you would like to order by entering its corresponding number from the list provided.")
            question = (
                f"~ Please enter a number between {MENU_LOW} and {MENU_HIGH}.\n    Enter: ")
            album_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            # Bringing in the 'MENU_LOW', 1, 'MENU_HIGH', 15 and 'question', "Please enter a number between 1 and 15. "

            # The program will subtract 1 from the entered number of albums that the user wants to order. This is to match the index number of the album list.
            album_ordered = album_ordered - 1
            # Picking out the album name from 'album_names' and is entered into the 'order_list'.
            order_list.append(album_names[album_ordered])
            # Picking out the album price from 'album_prices' and is entered into the 'order_cost'.
            order_cost.append(album_prices[album_ordered])
            print("    \033[1mAlbum Chosen:\033[0m {} \n                    \033[1m~ Price:\033[0m ${:.2f}" .format(
                album_names[album_ordered], album_prices[album_ordered]))
            # The {:.2f} rounds them up into 2 decimal places or 2 floats. The 0 appears now.
            # The album_names[count] will retrieve the name of the album at the current index, 'count', from the 'album_names' list.
            # The album_prices[count] will retrieve the price of the album at the current index, 'count', from the 'album_prices' list.
            # The output will be printed out through the format, "{album_number} {album_name} ${album_price}".
            # Ordered the first album, going back to order the rest of them, taking 1 off that total.
            num_albums = num_albums-1


# BUYING MORE ALBUMS. ~~~~~~~~~~~~~~
def order_more_album():
    # Asking the user to enter a number between 1 or 2.
    # A variable called 'question'.
    # Using 'f' to format the 'LOW' and 'HIGH' inside the '{}'.
    question = (
        f"~ Please enter a number between {LOW} and {HIGH}.\n    Enter: ")

    # Print statement that asks the user whether they want to BUY MORE ALBUMS or if they are FINISHED ORDERING.
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")
    print("If you wish to order more albums, this is your final time to do so.")
    print()
    print(
        "Do you want to \033[38;2;176;120;249m\033[1mBUY MORE ALBUMS\033[0m or are you \033[38;2;215;187;245m\033[1mFINISHED ORDERING?\033[0m\n")

    # Separate Print Statement lines.
    # Print statement asking the user to enter 1 for BUY MORE ALBUMS.
    print(
        "    ❀ To \033[38;2;176;120;249m\033[1mBUY MORE ALBUMS\033[0m, enter \033[38;2;176;120;249m\033[1m1\033[0m.")
    # Print statement asking the user to enter 2 for FINISHED ORDERING.
    print(
        "    ❀ If you have \033[38;2;215;187;245m\033[1mFINISHED ORDERING\033[0m, enter \033[38;2;215;187;245m\033[1m2\033[0m.\n")
    # Asking the user to enter their option.
    # The 'val_int' will make sure what the user's input is an integer.
    # New variable called, 'morealbums'.
    morealbums = val_int(LOW, HIGH, question)

    if morealbums == 1:  # If 'morealbums' is equal to 1, the user will be buying more albums.
        # Letting the user know that they will be ordering more albums.
        print(
            "\n\n\033[38;2;155;240;189m\033[1m~~❀ You are now ordering more albums. ❀~~\033[0m")
        print("\nPrinting the list of albums again.\n")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")
        # Making a variable (Will count through 15 times).
        # This is the total number of albums that the bot will be selling.
        number_albums = 15

        # Bringing in the code from the 'albums()' function to print the list of albums again.
        # The 'for' statement will create a loop that will start from 0 and will range through to the end of 'number_albums - 1' (from 0 to 14).
        print("\033[1mList of Albums Available:\033[0m\n")
        for count in range(number_albums):  # Taking 0.
            print(" \033[38;2;176;120;249m{})\033[0m  {} \n        \033[38;2;155;240;189m~ Price: ${:.2f}\033[0m\n".format(count+1,
                                                                                                                           album_names[count], album_prices[count]))  # Prints out each of the album names and album prices by its integer.
        # The {:.2f} rounds them up into 2 decimal places or 2 floats. The 0 appears now.
        # The count+1 will change the 2 Cool 4 Skool position from 0 to 1.
        # The album_names[count] will retrieve the name of the album at the current index, 'count', from the 'album_names' list.
        # The album_prices[count] will retrieve the price of the album at the current index, 'count', from the 'album_prices' list.
        # The output will be printed out through the format, "{album_number} {album_name} ${album_price}".

        # Bringing in the code from the 'order_album()' function to ask the user what albums they want to order again.
        # Ask for total number of albums for order.

        # Setting the variable 'NUM_LOW' to 1 and the variable 'NUM_HIGH' to 8.
        # NUM_LOW and NUM_HIGH are capitals which means that they are constant.
        # When they are constant, they do not change. They are literal.
        NUM_LOW = 1  # Set to literal 1.
        NUM_HIGH = 8  # Set to literal 8.

        # Setting the variable 'MENU_LOW' to 1 and the variable 'MENU_HIGH' to 15.
        MENU_LOW = 1  # Lowest number of available albums.
        MENU_HIGH = 15  # Highest number of available albums.

        # A variable called 'question'.
        # Using 'f' to format the 'NUM_LOW' and 'NUM_HIGH' inside the '{}'.
        question = (
            f"~ Please enter a number between {NUM_LOW} and {NUM_HIGH}.\n    Enter: ")

        # Asking the user how many albums they want to order.
        print("\nHow many albums do you want to order?")
        # The number of albums entered will go through the 'val_int()' function.
        # 'NUM_LOW' is 1, 'NUM_HIGH" is 8, 'question' is "Please enter a number between 1 and 8. ".
        num_albums = val_int(NUM_LOW, NUM_HIGH, question)
        # Choose album from the album list.
        # Used the 'for' statement to create a loop for the number of items that the user has chosen, found in num_albums.
        # Counting through how many albums have been chosen.
        for item in range(num_albums):
            # Another loop is made with the 'while' statement to ensure that the user can enter their chosen number.
            while num_albums > 0:
                print(
                    "\nChoose the album you would like to order by entering its corresponding number from the list provided.")
                question = (
                    f"~ Please enter a number between {MENU_LOW} and {MENU_HIGH}.\n    Enter: ")
                album_ordered = val_int(MENU_LOW, MENU_HIGH, question)
                # Bringing in the 'MENU_LOW', 1, 'MENU_HIGH', 15 and 'question', "Please enter a number between 1 and 15. "

                # The program will subtract 1 from the entered number of albums that the user wants to order. This is to match the index number of the album list.
                album_ordered = album_ordered - 1
                # Picking out the album name from 'album_names' and is entered into the 'order_list'.
                order_list.append(album_names[album_ordered])
                # Picking out the album price from 'album_prices' and is entered into the 'order_cost'.
                order_cost.append(album_prices[album_ordered])
                print("    \033[1mAlbum Chosen:\033[0m {} \n                    \033[1m~ Price:\033[0m ${:.2f}" .format(
                    album_names[album_ordered], album_prices[album_ordered]))
                # The {:.2f} rounds them up into 2 decimal places or 2 floats. The 0 appears now.
                # The album_names[count] will retrieve the name of the album at the current index, 'count', from the 'album_names' list.
                # The album_prices[count] will retrieve the price of the album at the current index, 'count', from the 'album_prices' list.
                # The output will be printed out through the format, "{album_number} {album_name} ${album_price}".
                # Ordered the first album, going back to order the rest of them, taking 1 off that total.
                num_albums = num_albums-1

    elif morealbums == 2:  # If 'confirm' is equal to 2, the order is cancelled.
        # Letting the user know that the order has been cancelled.
        print(
            "\n\n\033[38;2;155;240;189m\033[1m~~❀ You are now finished with ordering. ❀~~\033[0m\n")
        # print("\n\033[1m~~❀ Your Order has been Cancelled. ❀~~\033[0m")
        print("    Continuing with your order.")


# PRINT THE ORDER OUT. ~~~~~~~~~~~~~~
# This will be included if order is for delivery or for click and collect and names and price of each album - total cost including any delivery charge.
# Defining the function, 'print_order()'.
# Parameter used. The variable, 'del_click' is brought into the function, 'print_order()' and is used within it.
def print_order(del_click):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")

    # PRINTING ORDER OUT. ~~~~~~~~~~~~~~
    # This section is using the time module that we have imported.
    # Starting a while loop.
    while True:
        # The 'for' loop is used to iterate over a sequence of 4 elements using the 'range(4)' function, generating sequence between, and including, 0 to 3.
        # The 'i' takes in the variables of 0, 1, 2 and 3.
        # The loop will go through 4 times. Once the process is done, it will break out of the loop.
        for i in range(4):
            # Setting the suffix for the dots to appear.
            # When i = 0, so the string is empty (no '.' will appear).
            # When i = 1, the suffix is set to '.' ('.' will appear).
            # When i = 2, the suffix is set to '..' ('..' will appear).
            # When i = 3, the suffix is set to '...' ('...' will appear). This will be the end of the sequence.
            suffix = '.' * i if i < 3 else '...'
            # The program will print "Printing Order Out" and depending on the value of i, the program will print the number of dots after the message.
            print("Printing Order Out" + suffix, end='\r', flush=True)
            # Each '.' will appear after each second due to the '(1)'.
            time.sleep(1)
        # Breaks out of the while loop so that the rest of the program can continue.
        break

    total_cost = sum(order_cost)
    # Letting the user know that what is going to be printed will be their customer details.
    print(" \033[38;2;215;187;245m~❀ Your Customer Details:\033[0m")
    # If the variable, 'del_click' is equal to 'clickandcollect', the following will be printed.
    if del_click == "clickandcollect":
        print("     ❀ Your Order is for Click & Collect.")
        # Print statement that is used to display to the user the details of their order after being formatted.
        print(
            f"     \033[1m❀ Customer Name:\033[0m {customer_details['name']} \n     \033[1m❀ Customer Phone:\033[0m {customer_details['phone']}")
    # If the variable, 'del_click' is equal to 'delivery', the following will be printed.
    elif del_click == "delivery":
        print("     ❀ Your Order is for Delivery.")
        # Checking if 4 or less albums have been ordered.
        if len(order_list) <= 4:
            # The 'len' counts the list.
            # If there are 4 or less items ordered, make a print statement saying that there is a delivery charge of $9.00.
            print(
                "     ❀ Since you have ordered 4 or less albums, there will be a $9.00 delivery charge.")
            # Adding the $9.00 delivery charge to the total cost.
            total_cost += 9
        # Checking if 5 or more albums have been ordered.
        if len(order_list) >= 5:
            # If there are 5 or more items ordered, make a print statement saying that there will be no delivery charge.
            print(
                "     ❀ Since you have ordered 5 or more albums, your delivery will be free of charge.")
        # total_cost = total_cost + 9 will be used for adding the $9.00 delivery charge to the total cost of the order.
        # Print statement that is used to display to the user the details of their order after being formatted.
        print(f"     \033[1m❀ Customer Name:\033[0m {customer_details['name']} \n     \033[1m❀ Customer Phone:\033[0m {customer_details['phone']} \n     \033[1m❀ Customer Address:\033[0m {customer_details['house']} \n     \033[1m❀ Customer Street:\033[0m {customer_details['street']} \n     \033[1m❀ Customer Suburb:\033[0m {customer_details['suburb']}")
        # The 'f' at the front is a way to format.
        # For the 'Customer Name' in {customer_details['name']}, it will have the inserted value of the 'name' key from the 'customer_details' dictionary list.
        # For the 'Customer Phone' in {customer_details['phone']}, it will have the inserted value of the 'phone' key from the 'customer_details' dictionary list.
        # For the 'Customer Address' in {customer_details['house']}, it will have the inserted value of the 'house' key from the 'customer_details' dictionary list.
        # For the 'Customer Street' in {customer_details['street']}, it will have the inserted value of the 'street' key from the 'customer_details' dictionary list.
        # For the 'Customer Suburb' in {customer_details['suburb']}, it will have the inserted value of the 'suburb' key from the 'customer_details' dictionary list.
    print()
    # Letting the user know that what is going to be printed will be their order details.
    print(" \033[38;2;215;187;245m~❀ Your Order Details:\033[0m")
    count = 0  # 25.70 is at the position of 0.
    # The 'for' statement will create a loop that will go through each item in the 'order_list'.
    for item in order_list:
        print("     ❀ \033[1mAlbum Ordered:\033[0m {}  \033[1m~~\033[0m  \033[1mAlbum Cost:\033[0m ${:.2f}" .format(
            item, order_cost[count]))  # Will print the formatted albums ordered and their corresponding price.
        # The ':.2f' will round the cost of each ordered album to 2 decimal places.
        # The 'count' variable keeps track of the correct index in the 'order_cost' list.
        # Adding 1 to the 'count' variable so that next time, when the function picks out a different item, it will become a different number.
        count = count+1
    print()
    # Letting the user know that what is going to be printed will be their total order cost.
    print(" \033[38;2;215;187;245m~❀ Total Order Cost:\033[0m")
    # The ':.2f' will round the sum of the order to 2 decimal places.
    print(f"     ${total_cost:.2f}")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")


# CONFIRM OR CANCEL THE ORDER. ~~~~~~~~~~~~~~
# Ability to cancel the current order or to proceed with a new order.
# Parameter used to bring in the variable, 'del_click' into this function of 'confirm_cancel()' to check if the order is for Click and Collect or Delivery.
def confirm_cancel(del_click):
    # The CONFIRM or CANCEL order options.

    # Asking the user to enter a number between 1 or 2.
    # A variable called 'question'.
    # Using 'f' to format the 'LOW' and 'HIGH' inside the '{}'.
    question = (
        f"~ Please enter a number between {LOW} and {HIGH}.\n    Enter: ")

    print("Please confirm your order.\n")
    # Letting the user know that entering 1 will CONFIRM their order.
    print(
        "    ❀ To \033[1;38;2;155;240;189mCONFIRM\033[0m, enter \033[1;38;2;155;240;189m1\033[0m.")
    # Letting the user know that entering 2 will CANCEL their order.
    print(
        "    ❀ To \033[1;38;2;255;116;116mCANCEL\033[0m, enter \033[1;38;2;255;116;116m2\033[0m.\n")

    # 'LOW' is 1, 'HIGH" is 2, 'question' is "Please enter a number between 1 and 2. ".
    confirm = val_int(LOW, HIGH, question)

    if confirm == 1:  # If 'confirm' is equal to 1, the order is confirmed.
        # Letting the user know that the order has been confirmed.
        print(
            "\n\n\033[38;2;155;240;189m\033[1m~~❀ Your Order has been Confirmed! ❀~~\033[0m")
        # Bringing in the parameter of 'del_click' checks if Click and Collect was chosen.
        if del_click == "clickandcollect":
            # Print statement printed only when click and collect was chosen.
            print(
                "\n    You will receive a text message shortly to know when your order is ready for collection.")
            # The function of starting a new order or exiting out of the Bangtan Bot program will run after confirming.
            new_exit()
        # Bringing in the parameter of 'del_click' checks if Delivery was chosen.
        elif del_click == "delivery":
            # Print statement printed only when Delivery was chosen.
            print(
                "\n    You will soon receive text messages to notify you of the status of your delivery.")
            # The function of starting a new order or exiting out of the Bangtan Bot program will run after confirming.
            new_exit()

    elif confirm == 2:  # If 'confirm' is equal to 2, the order is cancelled.
        # Letting the user know that the order has been cancelled.
        print(
            "\n\n\033[38;2;255;116;116m\033[1m~~❀ Your Order has been Cancelled. ❀~~\033[0m")
        print("\n    You can RESTART your order or EXIT the Bangtan Bot.")
        # The function of starting a new order or exiting out of the Bangtan Bot program will run after cancelling.
        new_exit()


# START A NEW ORDER OR EXIT OUT OF THE BANGTAN BOT PROGRAM. ~~~~~~~~~~~~~~
# Option to create a new order or to exit out of the program.
# Defines the 'sys' function class for the 'sys.exit' so that it exits the program.
def new_exit():

    # Setting the variable 'LOW' to 1 and the variable 'HIGH' to 2.
    # LOW and HIGH are capitalized which means that they are constant.
    # When they are constant, they do not change. They are literal.
    # Using the 'LOW' parameter.
    LOW = 1  # Set to literal 1.
    # Using the 'HIGH' parameter.
    HIGH = 2  # Set to literal 2.

    # Asking the user to enter a number between 1 or 2.
    # A variable called 'question'.
    # Using 'f' to format the 'LOW' and 'HIGH' inside the '{}'.
    question = (
        f"~ Please enter a number between {LOW} and {HIGH}.\n    Enter: ")

    # Asking the user if they want to start another order or to exit the Bangtan Bot program.
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")
    print("Do you want to start another Order or Exit?\n")
    # Input of 1 will make another order.
    print(
        "    ❀ To \033[1;38;2;155;240;189mSTART ANOTHER ORDER\033[0m, enter \033[1;38;2;155;240;189m1\033[0m.")
    # Input of 2 will exit the Bangtan Bot program.
    print(
        "    ❀ To \033[1;38;2;255;116;116mEXIT\033[0m, enter \033[1;38;2;255;116;116m2\033[0m.\n")

    # 'LOW' is 1, 'HIGH" is 2, 'question' is "Please enter a number between 1 and 2. ".
    confirm = val_int(LOW, HIGH, question)

    if confirm == 1:  # If 'confirm' is equal to 1, a new order will be made.
        # Letting the user know that a new order will be made.
        print(
            "\n\n\033[38;2;155;240;189m\033[1m~~❀ You Chose to Create a New Order. ❀~~\033[0m\n\n\n\n")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")
        # Clearing the data from the current order from all lists.
        order_list.clear()  # Clearing data from the list, 'order_list'.
        order_cost.clear()  # Clearing data from the list, 'order_cost'.
        # Clearing data from the list, 'customer_details'.
        customer_details.clear()

        # STARTING NEW ORDER. ~~~~~~~~~~~~~~
        # This section is using the time module that we have imported.
        # Starting a while loop.
        while True:
            # The 'for' loop is used to iterate over a sequence of 4 elements using the 'range(4)' function, generating sequence between, and including, 0 to 3.
            # The 'i' takes in the variables of 0, 1, 2 and 3.
            # The loop will go through 4 times. Once the process is done, it will break out of the loop.
            for i in range(4):
                # Setting the suffix for the dots to appear.
                # When i = 0, so the string is empty (no '.' will appear).
                # When i = 1, the suffix is set to '.' ('.' will appear).
                # When i = 2, the suffix is set to '..' ('..' will appear).
                # When i = 3, the suffix is set to '...' ('...' will appear). This will be the end of the sequence.
                suffix = '.' * i if i < 3 else '...'
                # The program will print "Starting New Order" and depending on the value of i, the program will print the number of dots after the message.
                print("New Order" + suffix, end='\r', flush=True)
                # Each '.' will appear after each second due to the '(1)'.
                time.sleep(1)
            # Breaks out of the while loop so that the rest of the program can continue.
            break

        main()

    elif confirm == 2:  # If 'confirm' is equal to 2, the program will stop.
        # Letting the user know that they will now exit out of the Bangtan Bot program.
        print(
            "\n\n\033[38;2;255;116;116m\033[1m~~❀ You Chose to Exit the Program. ❀~~\033[0m")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⟭⟬\n")
        order_list.clear()  # Clearing data from the list, 'order_list'.
        order_cost.clear()  # Clearing data from the list, 'order_cost'.
        # Clearing data from the list, 'customer_details'.
        customer_details.clear()

        # EXITING PROGRAM. ~~~~~~~~~~~~~~
        # This section is using the time module that we have imported.
        # Starting a while loop.
        while True:
            # The 'for' loop is used to iterate over a sequence of 4 elements using the 'range(4)' function, generating sequence between, and including, 0 to 3.
            # The 'i' takes in the variables of 0, 1, 2 and 3.
            # The loop will go through 4 times. Once the process is done, it will break out of the loop.
            for i in range(4):
                # Setting the suffix for the dots to appear.
                # When i = 0, so the string is empty (no '.' will appear).
                # When i = 1, the suffix is set to '.' ('.' will appear).
                # When i = 2, the suffix is set to '..' ('..' will appear).
                # When i = 3, the suffix is set to '...' ('...' will appear). This will be the end of the sequence.
                suffix = '.' * i if i < 3 else '...'
                # The program will print "Exiting Program" and depending on the value of i, the program will print the number of dots after the message.
                print("Exiting Program" + suffix, end='\r', flush=True)
                # Each '.' will appear after each second due to the '(1)'.
                time.sleep(1)
            # Breaks out of the while loop so that the rest of the program can continue.
            break

        sys.exit()  # Exiting out of the program.


# MAIN FUNCTION. ~~~~~~~~~~~~~~
# The main function will call the other functions (components).
# This is where I am defining the main function of the main program.
# This function is going to be responsible for running the whole program.
# This function is defined as 'main()'.
def main():
    # Purpose of the main() function.
    '''
    Purpose: To run all functions.
    Parameters: None.
    Returns: None.
    '''
    # Action being executed (the 'welcome()' function. Called within the 'main()' function).
    welcome()
    # Action being executed (the 'order_type()' function. Called within the 'main()' function).
    # 'del_click' is equal to what comes out of the function, 'order_type()'.
    del_click = order_type()
    # Action being executed (the 'albums()' function. Called within the 'main()' function).
    albums()
    # Action being executed (the 'order_album()' function. Called within the 'main()' function).
    order_album()
    # Action being executed (the 'order_more_album()' function. Called within the 'main()' function).
    order_more_album()
    # Parameter is used to bring one variable from one function to another.
    # The result of the variable, 'del_click', click and collect or delivery, will be sent to this function.
    print_order(del_click)
    # Parameter is used to bring one variable from one function to another.
    # The result of the variable, 'del_click', click and collect or delivery, will be sent to this function.
    confirm_cancel(del_click)


# Call the main function.
# Calling the main function will execute all of the functions that are called within it.
main()
