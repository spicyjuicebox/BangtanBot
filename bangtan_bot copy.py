# BangtanBot Program.

# Bugs - (List bugs here.)
# Bug 03/07/2023: When entering input for 'name', it accepts numbers and other characters ('!') when it should not.
# Bug 03/07/2023: When entering input for 'phone', it accepts letters and other characters ('!') when it should not.

# Known Bugs - (List known bugs here.)


# IMPORT STATEMENTS found here. ~~~~~~~~~~~~~~
import sys # Importing 'sys' is the function class for the 'sys.exit' so that it exits the program.
import random # Importing the random module. Provides function for generating random numbers and choosing something random from the selection.
import time # Importing 'time' will bring the library module, 'time' into the program. This will be useful for any time-related functions.
from random import randint # Choosing random integer.


# CONSTANTS found here. ~~~~~~~~~~~~~~
# These LOW and HIGH constants are now available to every function when brought out of the other functions and up here.
# Setting the variable 'LOW' to 1 and the variable 'HIGH' to 2.
# LOW and HIGH are capitals which means that they are constant.
# When they are constant, they do not change. They are literal.
# Using the 'LOW' parameter.
LOW = 1 # Set to literal 1.
# Using the 'HIGH' parameter.
HIGH = 2 # Set to literal 2.

# The pohone numbers in New Zealand are generally 8 to 11 digits long.
# The program should check if the phone number being entered is only ranging and including from 8 to 11 digits long.
# Setting the variables.
# These are parameters, they are used in the function, 'check_phone()'.
PH_LOW = 8 # Lowest amount of digits allowed to be entered.
PH_HIGH = 11 # Highest amount of digits allowed to be entered.


# LISTS found here. ~~~~~~~~~~~~~~
# LIST OF RANDOM NAMES. ~~~~~~~~~~~~~~
# The line below is a list for 'names' with the sequence of strings for each name.
names = ["Jungkook", "Jimin", "V", "J-Hope", "Suga", "RM", "Jin", "Jaehyun", "Felix", "Sunghoon"]

# LIST OF ALBUM NAMES. ~~~~~~~~~~~~~~
# This is a list that is named, 'album_names'. This list stores the information of the list of albums that the program will be selling.
# The list is defined using the square brackets, '[]'. Inside these are strings that are separated by commas and are enclosed by single quotes to indicate that each are strings.
# The order of the items in this list will be written out in the same order when printed.
album_names = ['2 Cool 4 Skool','O!RUL8,2?','Skool Luv Affair','No More Dream','The Most Beautiful Moment In Life Pt.1','The Most Beautiful Moment In Life Pt.2','The Most Beautiful Moment In Life: Young Forever','WINGS','Love Yourself: Her','Love Yourself: Tear','Love Yourself: Answer','Map of the Soul: Persona','Map of the Soul: 7','BE','Butter']
# The 2 Cool 4 Skool album is at position 0.

# LIST OF ALBUM PRICES. ~~~~~~~~~~~~~~
# Another list variable that is named, 'album_prices'.
# The list is defined using the square brackets, '[]'. Inside these are strings that are separated by commas and each represent the price of each of the albums to be sold.
# The order of the prices or numbers in this list will be written out in the same order when printed and aligns itself with the album_names list.
album_prices = [25.70, 32.20, 28.40, 40.20, 40.10, 45.70, 62.50, 45.80, 50.50, 58.40, 60.80, 52.20, 90.50, 55.50, 40.20]
# The first 25.70 is at position 0.
# This lines up with the album_names of '2 Cool 4 Skool' with it being at position 0.

# LIST OF STORED ORDERED ALBUMS. ~~~~~~~~~~~~~~
order_list = []

# LIST OF STORED ALBUM PRICES. ~~~~~~~~~~~~~~
order_cost = []


# DICTIONARY TO STORE INFORMATION found here. ~~~~~~~~~~~~~~
# Customer Details Dictionary
# Curly brackets indicate a dictionary (stores information - customer details). Holds information, better than a list.
customer_details = {}


# VALIDATION found here. ~~~~~~~~~~~~~~
# Validates Inputs to check if they are blank.
# Function - Everytime you want to check if something is not blank, it is sent to this function. Taking a question/variable from somewhere else.
def not_blank(question): # This is a parameter. It brings variables ('question') in from different places in our code. Parameter is anything inside the brackets. Bringing in the question.
    # What the user enters in this input line of code will be assigned to the variable, 'name'.
    # Assigning the value, 'False', to the variable, 'valid'.
    # By assigning it this way, it is indicated that the condition for the valid variable is not satisfied.
    # It is used to track the values being entered by the user into the program and will control the flow of the program.
    valid = False
    # Starting a while loop as long as the condition is 'not valid'.
    while not valid:
        # The question is a variable in the input section. It is then brought up as a parameter.
        response = input(question) # Response to the question.  Displaying the question.
        if response != "": # Break will break out of the loop. Here, we are going to return the response back out with the function. Asking for a response and is checking to see if it is blank.
            return response.title() # Changes all to title class (will capitalise the first letter entered).  # Also kicks out of the loop.  It will return it back down and be entered into the dictionary.
        # When the condition for the 'if' statement is false, the program will skip to the 'else' code.
        else:
            # The 'else' statement will print this line of code.
            print("This cannot be blank.")


# VALIDATION found here. ~~~~~~~~~~~~~~
# Defining the function, check_string().
# Using the 'isalpha' to check if the input is all alphabetical.
def check_string(question): # Bringing in the variable, 'question', into the function.
    while True:
        # Using the variable, 'response'. This is a parameter.
        response = input(question) # The answer to the question will go to the 'response' variable.
        # Setting up the variable, 'x'.
        x = response.isalpha()
        # The 'isalpha' checks if the string is using the alphabet (alphabetical).
        # Checking if the response is alphabetical or not.
        # Checking if there are numbers or other characters being used in the response.

        # If it is not alphabetical, run the 'if' statement.
        if x == False:
            print("Input must only contain letters.")
            # Will continue to run the loop until correct input.
        else:
            return(response.title()) # The response will be printed and the first letter will be capitalised.
# This function will be used whenever a function is asking for a name or for the user's address details (street name and suburb).


# VALIDATION found here. ~~~~~~~~~~~~~~
# Validating the menu for the user to choose either the Click & Collect or Delivery option.
# Validating the inputs to check if they are an integer.
# The function is asking the user for a number.
def val_int(low, high, question): # Parameter, using three variables in the function, 'order_type()'.
    # The 'low' becomes 1, 'high' becomes 2, 'question' becomes "Please enter a number between 1 and 2. ".
    # The 'while True' loop will create an infinite loop.
    while True:
        try: # The try statement will catch and handle except statements. Trying to get input from the user.
            # Asking the user to enter their option.
            # The 'int' will make sure what the user inputs is an interger.
            # Using the 'question' parameter.
            # Trying the number.
            num = int(input(question)) # The print statement prints and after this, the user enters their input. Trying to get an integer.

            # The 'and' combines these two conditions. Both conditions must be true for the whole expression to be true.
            # First condition checks if the num is an integer that is greater than or equal to 1, low.
            # Second condition checks if the num is an integer that is less than or equal to 2, high.
            # If both conditions are met, then the program will run either of the if or elif statement.
            # If both or either of the conditions are not met, then the program will skip the if or elif statements and skip to the next part of the code.
            if num >= low and num <= high: # Using the 'low' and 'high' parameter.
                # Storing 1 or 2 into the variable, 'answer'.
                return num # Return means that this number, 1, low, or 2, high, is stored into the variable, answer. Breaks out of loop.
                # Will return the number back to the 'delivery' variable in the 'order_type()' function.
            # When input is a number that is not 1, low, or 2, high, the program will run the else statement.
            else:
                print(f"Please enter a number between {low} and {high}. ") # Letting the user know why their input did not work.
        
        # When the user does not enter either '1' or '2', the ValueError will print these error messages.
        except ValueError:
            print("That is not a valid number.")
            print(f"Please enter a number between {low} and {high}. ")


# VALIDATION found here. ~~~~~~~~~~~~~~
# Validating if the input for the phone number is all integers.
# Defining the function, check_phone().
# This function will be using parameters.
def check_phone(PH_LOW, PH_HIGH, question):
    # Bringing in the variable, 'question', into the function.
    # Bringing in the variable, 'PH_LOW', for 8, into the function.
    # Bringing in the variable, 'PH_HIGH', for 11, into the function.
    # Starting a loop.
    while True:
        try: # Trying if the input is an integer.
            # Setting a variable called, 'num' for the phone number input.
            num = int(input(question)) # Bringing in the 'question' variable.
            # The response to the question will be entered into the 'num' variable.
            # Setting a variable called, 'test_num' to test the number input.
            test_num = num
            count = 0 # The 'count' counts through how many digits are in the input.
            while test_num > 0:
                # Taking the number and dividing the test_num by 11.
                test_num = test_num//10
                count = count + 1 # Adding 1 to the count variable.
            # Setting up the two conditions in the 'if' statement.
            if count >= PH_LOW and count <= PH_HIGH:
                # Returning breaks out of the loop.
                return str(num) # Made into a string because if not, the first digit being a 0 will be removed after printing.
                # Leaving it as it is.
            # If the input phone number is not between and including 8 to 11 digits, the error message will print.
            else:
                print("NZ phone numbers must be 8 to 11 digits long.")
        # If the input phone number does not contain all numbers, the error message will print.\
        except ValueError:
            print("Please enter your phone number using only numbers.")
            # Should go into a loop until valid input is entered.


# WELCOME MESSAGE WITH RANDOMLY GENERATED NAME. ~~~~~~~~~~~~~~
# This is a function for the welcome part of the main program.
# This function is made to generate a random name from the 'names' list above, then print out a welcome message.
# The welcome message will incluce the selected, randomly generated name.
# Defining the function, 'welcome()'.
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
    # START PRINTING THE GREETING. ~~~~~~~~~~~~~~
    print("2.. 3.. Hello, we are BTS!")
    print("Thank you for choosing...")
    # The \033[95m" + will make the colour of the text in the print code to the colour purple.
    # The '38' indicates to the program that the text is going to change colour.
    # The '2' indicates to the program that a custom RGB colour will be used.
    # The '176;120;249' are the same values of the hex code, #B078F9.
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
                                                                                                                                
    """ + "\033[0m") # The line of code, \033[0m" will ensure that the colour will only affect this print statement.
    # If I do not do the code above, then the other print statements underneath BANGTAN BOT will also be of the colour purple.
    print("We are a trusted chat bot that will help you make online orders for BTS albums!")
    print("My name is {}!". format(name)) # The '{}' will be replaced by what we have formatted, 'name', so that it is replaced with a randomly generated name from the list.
    print("I will be here to help you make your online orders!")


# MENU FOR CLICK & COLLECT/DELIVERY. ~~~~~~~~~~~~~~
# Menu for the user to choose either the Click & Collect or Delivery option.
def order_type():
    del_click = "" # This variable is equal to default, empty, blank string.
    # This variable will change to 'clickandcollect' if 1 is entered.
    # This variable will change to 'delivery' if 2 is entered.


    # Asking the user to enter a number between 1 or 2 for testing.
    # A variable called 'question'.
    # Using 'f' to format the 'LOW' and 'HIGH' inside the '{}'.
    question = (f"Please enter a number between {LOW} and {HIGH}. ")


    # Print statement that asks the user whether they want their order to be for Click & Collect or Delivery.
    print ("Do you want your order to be CLICK & COLLECT or DELIVERED to you?")

    # Separate Print Statement lines.
    print ("For CLICK & COLLECT, enter 1.") # Print statement asking the user to enter d for Delivery.
    print ("For DELIVERY, enter 2.") # Print statement asking the user to enter c for Click & Collect.
    # Asking the user to enter their option.
    # The 'int' will make sure what the user inputs is an integer.
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1: # Checking if what is entered is '1'.
        print ("Click & Collect") # If '1' is entered, 'Click & Collect' will be printed.
        # If Click & Collect is chosen, then the variable, 'del_click', will equal to "clickandcollect".
        del_click = "clickandcollect" # This will change the 'del_click' variable.
        clickandcollect_info() # Will run the clickandcollect() function.
    # Only other valid option will be 2.
    else:
        print ("Delivery") # If '2' is entered, 'Delivery' will be printed.
        # If Delivery is chosen, then the variable, 'del_click', will equal to "delivery".
        delivery_info() # Will run the delivery() function.
        del_click = "delivery" # This will change the 'del_click' variable.
    return del_click # This will return the 'del_click' variable back down to the main() function at 'del_click = order_type()'.


# CLICK & COLLECT INFORMATION. ~~~~~~~~~~~~~~
# Question (variable) comes from here.
# Defining the function, 'clickandcollect()' for the click and collect component of the main program.
def clickandcollect_info():
    question = ("Please enter your name. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'name'.
    # Getting the customer details name from the above function, bringing in the question.
    customer_details['name'] = check_string(question) # Customer name will go to the function for 'check_string(question)' to check if the input is all alphabetical.
    print(customer_details['name'])


    question = ("Please enter your phone number. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'phone'.
    # Getting the customer details phone from the above function, bringing in the question.
    customer_details['phone'] = check_phone(PH_LOW, PH_HIGH, question) # Customer phone number will go to the function for 'check_phone(PH_LOW, PH_HIGH, question)' to check if the input is all numbers.
    print(customer_details['phone'])
    print(customer_details)


# DELIVERY INFORMATION. ~~~~~~~~~~~~~~
# Question (variable) comes from here.
# Defining the function, 'delivery' for the delivery component of the main program.
def delivery_info():
    # Basic Instructions
    # Question (variable) comes from here.
    question = ("Please enter your name. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'name'.
    # Getting the customer details name from the above function, bringing in the question.
    customer_details['name'] = check_string(question) # Customer name will go to the function for 'check_string(question)' to check if the input is all alphabetical.
    print(customer_details['name'])


    question = ("Please enter your phone number. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'phone'.
    # Getting the customer details phone from the above function, bringing in the question.
    customer_details['phone'] = check_phone(PH_LOW, PH_HIGH, question) # Customer phone number will go to the function for 'check_phone(PH_LOW, PH_HIGH, question)' to check if the input is all numbers.
    print(customer_details['phone'])


    question = ("Please enter your house number. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'house'.
    # Getting the customer details phone from the above function, bringing in the question.
    customer_details['house'] = not_blank(question) # Customer name will go to the function for 'not_blank'.
    print(customer_details['house'])


    question = ("Please enter your street name. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'street'.
    # Getting the customer details phone from the above function, bringing in the question.
    customer_details['street'] = check_string(question) # Customer name will go to the function for 'check_string(question)' to check if the input is all alphabetical.
    print(customer_details['street'])


    question = ("Please enter your suburb. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'suburb'.
    # Getting the customer details phone from the above function, bringing in the question.
    customer_details['suburb'] = check_string(question) # Customer name will go to the function for 'check_string(question)' to check if the input is all alphabetical.
    print(customer_details['suburb'])


# BTS ALBUMS. ~~~~~~~~~~~~~~
# Defining the function for the albums as albums().
# This function will be responsible for displaying the album names, album prices and their corresponding index numbers.
def albums():
    # Making a variable (Will count through 15 times).
    number_albums = 15 # This is the total number of albums that the bot will be selling.

    # The 'for' statement will create a loop that will start from 0 and will range through to the end of 'number_albums - 1' (from 0 to 14).
    for count in range (number_albums): # Taking 0.
        print("{} {} ${:.2f}" .format(count+1, album_names[count],album_prices[count])) # Prints out each of the album names and album prices by its integer.
        # The {:.2f} rounds them up into 2 decimal places or 2 floats. The 0 appears now.
        # The count+1 will change the 2 Cool 4 Skool position from 0 to 1.
        # The album_names[count] will retrieve the name of the album at the current index, 'count', from the 'album_names' list.
        # The album_prices[count] will retrieve the price of the album at the current index, 'count', from the 'album_prices' list.
        # The output will be printed out through the format, "{album_number} {album_name} ${album_price}".


# CHOOSING THE NUMBER OF ALBUMS TO PURCHASE. ~~~~~~~~~~~~~~
# Choosing which items to purchase - print each album ordered with cast.
# Defining the function for the ordering of the albums as order_album().
def order_album():
    # Ask for total number of albums for order.
    num_albums = 0 # This variable has the value of 0.

    # Setting the variable 'NUM_LOW' to 1 and the variable 'NUM_HIGH' to 8.
    # NUM_LOW and NUM_HIGH are capitals which means that they are constant.
    # When they are constant, they do not change. They are literal.
    NUM_LOW = 1 # Set to literal 1.
    NUM_HIGH = 8 # Set to literal 8.

    MENU_LOW = 1 # Lowest number of available albums.
    MENU_HIGH = 15 # Highest number of available albums.


    # Asking the user to enter a number between 1 or 2 for testing.
    # A variable called 'question'.
    # Using 'f' to format the 'NUM_LOW' and 'NUM_HIGH' inside the '{}'.
    question = (f"Please enter a number between {NUM_LOW} and {NUM_HIGH}. ")

    
    # Asking the user how many albums they want to order.
    print("How many albums do you want to order?")
    # The number of albums entered will go through the 'val_int()' function.
    # 'NUM_LOW' is 1, 'NUM_HIGH" is 8, 'question' is "Please enter a number between 1 and 8. ".
    num_albums = val_int(NUM_LOW, NUM_HIGH, question)
    # Choose album from the album list.
    # Used the 'for' statement to create a loop for the number of items that the user has chosen, found in num_albums.
    for item in range(num_albums): # Counting through how many albums have been chosen.
        # Another loop is made with the 'while' statement to ensure that the user can enter their chosen number.
        while num_albums > 0:
            print("Please choose the albums you would like to order by entering its corresponding number from the list provided. ")
            question = (f"Please enter a number between {MENU_LOW} and {MENU_HIGH}. ")
            album_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            # Bringing in the 'MENU_LOW', 1, 'MENU_HIGH', 15 and 'question', "Please enter a number between 1 and 15. "


            album_ordered = album_ordered -1 # The program will subtract 1 from the entered number of albums that the user wants to order. This is to match the index number of the album list.
            order_list.append(album_names[album_ordered]) # Picking out the album name from 'album_names' and is entered into the 'order_list'.
            order_cost.append(album_prices[album_ordered]) # Picking out the album price from 'album_prices' and is entered into the 'order_cost'.
            print("{} ${:.2f}" .format(album_names[album_ordered],album_prices[album_ordered]))
            # The selected albums and their names and prices will be displayed through the format, "Album name $Album price".
            # The {:.2f} rounds them up into 2 decimal places or 2 floats. The 0 appears now.
            # The album_names[count] will retrieve the name of the album at the current index, 'count', from the 'album_names' list.
            # The album_prices[count] will retrieve the price of the album at the current index, 'count', from the 'album_prices' list.
            # The output will be printed out through the format, "{album_number} {album_name} ${album_price}".
            num_albums = num_albums-1 # Ordered the first album, going back to order the rest of them, taking 1 off that total.


# PRINT THE ORDER OUT. ~~~~~~~~~~~~~~
# This will be included if order is for delivery or for click and collect and names and price of each album - total cost including any delivery charge.
# Defining the function, 'print_order()'.
def print_order(del_click): # Parameter used. The variable, 'del_click' is brought into the function, 'print_order()' and it used within it.
    print()
    total_cost = sum(order_cost)
    print("Your Customer Details") # Letting the user know that was is going to be printed will be their customer details.
    # If the variable, 'del_click' is equal to 'clickandcollect', the following will be printed.
    if del_click == "clickandcollect":
        print("Your Order is for Click and Collect.")
        # Print statement that is used to display to the user the details of their order after being formatted.
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    # If the variable, 'del_click' is equal to 'delivery', the following will be printed.
    elif del_click == "delivery":
        print("Your Order is for Delivery.")
        if len(order_list) >= 5: # Checking if 5 or more albums have been ordered.
            # The 'len' counts the list.
            # If there are 5 or more items ordered, make a print statement saying that there is a delivery charge of $9.00.
            print("Since you have ordered 5 or more albums, there will be a $9.00 delivery charge.")
            total_cost += 9  # Adding the $9.00 delivery charge to the total cost.
        #print("Since you have ordered 5 or more albums, there will be a $9.00 delivery charge.")
        #total_cost = total_cost + 9 # Adding the $9.00 delivery charge to the total cost of the order.
        # Print statement that is used to display to the user the details of their order after being formatted.
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} \nCustomer Street: {customer_details['street']} \nCustomer Suburb: {customer_details['suburb']}")
        # The 'f' at the front is a way to format.
        # For the 'Customer Name' in {customer_details['name']}, it will have the inserted value of the 'name' key from the 'customer_details' dictionary list.
        # For the 'Customer Phone' in {customer_details['phone']}, it will have the inserted value of the 'phone' key from the 'customer_details' dictionary list.
        # For the 'Customer Address' in {customer_details['house']}, it will have the inserted value of the 'house' key from the 'customer_details' dictionary list.
        # For the 'Customer Street' in {customer_details['street']}, it will have the inserted value of the 'street' key from the 'customer_details' dictionary list.
        # For the 'Customer Suburb' in {customer_details['suburb']}, it will have the inserted value of the 'suburb' key from the 'customer_details' dictionary list.
    print()
    print("Your Order Details") # Letting the user know that was is going to be printed will be their order details.
    count = 0 # 25.70 is at the position of 0.
    # The 'for' statement will create a loop that will go through each item in the 'order_list'.
    for item in order_list:
        print("Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count])) # Will print the formatted albums ordered and their corresponding price.
        # The ':.2f' will round the cost of each ordered album to 2 decimal places.
        # The 'count' variable keeps track of the correct index in the 'order_cost' list.
        count = count+1 # Adding 1 to the 'count' variable so that next time, when the function picks out a different item, it will become a different number.
    print()
    print("Total Order Cost") # Letting the user know that was is going to be printed will be their total order details.
    print(f"${total_cost:.2f}") # The ':.2f' will round the sum of the order to 2 decimal places.


# CONFIRM OR CANCEL THE ORDER. ~~~~~~~~~~~~~~
# Ability to cancel the current order or to proceed with a new order.
def confirm_cancel(del_click): # Paramter used to bring in the variable, 'del_click' into this function of 'confirm_cancel()' to check if the order is for Click and Collect or Delivery.
    # The CONFIRM or CANCEL order options.


    # Asking the user to enter a number between 1 or 2 for testing.
    # A variable called 'question'.
    # Using 'f' to format the 'LOW' and 'HIGH' inside the '{}'.
    question = (f"Please enter a number between {LOW} and {HIGH}. ")


    print ("Please confirm your order.")
    print ("To CONFIRM, please enter 1.") # Letting the user know that entering 1 will CONFIRM their order.
    print ("To CANCEL, please enter 2.") # Letting the user know that entering 2 will CANCEL their order.

    # 'LOW' is 1, 'HIGH" is 2, 'question' is "Please enter a number between 1 and 2. ".
    confirm = val_int(LOW, HIGH, question)

    if confirm == 1: # If 'confirm' is equal to 1, the order is confirmed.
        # Letting the user know that the order has been confirmed.
        print("Your Order has been Confirmed.")
        if del_click == "clickandcollect": # Bringing in the parameter of 'del_click' checks if Click and Collect was chosen.
            # Print statement printed only when click and collect was chosen.
            print("Order Confirmed. You will receive a text message shortly to know when your order is ready to click and collect.")
            new_exit() # The function of starting a new order to exiting out of the Bangtan Bot program will run after confirming.
        elif del_click == "delivery": # Bringing in the parameter of 'del_click' checks if Delivery was chosen.
            # Print statement printed only when Delivery was chosen.
            print("You will soon receive text messages to notify you of the status of your delivery.")
            new_exit() # The function of starting a new order to exiting out of the Bangtan Bot program will run after confirming.


        elif confirm == 2: # If 'confirm' is equal to 2, the order is cancelled.
            # Letting the user know that the order has been cancelled.
            print("Your Order has been Cancelled.")
            print("You can restart your order or exit the Bangtan Bot.")
            new_exit() # The function of starting a new order to exiting out of the Bangtan Bot program will run after cancelling.
            # When input is a number that is not 1 or 2.


# START A NEW ORDER OR EXIT OUT OF THE BANGTAN BOT PROGRAM. ~~~~~~~~~~~~~~
# Option to create a new order or to exit out of the program.
# Defines the 'sys' function class for the 'sys.exit' so that it exits the program.
def new_exit():

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

    # Asking the user if they want to start another order or to exit the Bangtan Bot program.
    print ("Do you want to start another Order or Exit?")
    print ("To start another order, please enter 1.") # Input of 1 will make another order.
    print ("To exit the BOT, please enter 2.") # Input of 2 will exit the Bangtan Bot program.

    # 'LOW' is 1, 'HIGH" is 2, 'question' is "Please enter a number between 1 and 2. ".
    confirm = val_int(LOW, HIGH, question)

    if confirm == 1: # If 'confirm' is equal to 1, a new order will be made.
        print ("New Order") # Letting the user know that a new order will be made.
        # Clearing the data from the current order from all lists.
        order_list.clear() # Clearing data from the list, 'order_list'.
        order_cost.clear() # Clearing data from the list, 'order_cost'.
        customer_details.clear() # Clearing data from the list, 'customer_details'.
        main()

    elif confirm == 2: # If 'confirm' is equal to 2, the program will stop.
        print ("Exit") # Letting the user know that they will now exit out of the Bangtan Bot program.
        order_list.clear() # Clearing data from the list, 'order_list'.
        order_cost.clear() # Clearing data from the list, 'order_cost'.
        customer_details.clear() # Clearing data from the list, 'customer_details'.
        sys.exit() # Exiting out of the program.


# MAIN FUNCTION. ~~~~~~~~~~~~~~
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
    del_click = order_type() # Action being executed (the 'order_type()' function. Called within the 'main()' function.
    # 'del_click' is equal to what comes out of the function, 'order_type()'.
    albums() # Action being executed (the 'albums()' function. Called within the 'main()' function.
    order_album() # Action being executed (the 'order_album()' function. Called within the 'main()' function.
    # Parameter used to bring one variable from one function to another.
    print_order(del_click) # The result of the variable, 'del_click', click and collect or delivery, will be sent to this function.
    # Parameter used to bring one variable from one function to another.
    confirm_cancel(del_click) # The result of the variable, 'del_click', click and collect or delivery, will be sent to this function.


# Call the main function.
# Since the welcome() function was called within the main() function, then this main() function will
# - execute the welcome() function when called.
main()