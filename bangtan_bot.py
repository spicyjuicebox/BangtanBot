# BangtanBot Program.

# Bugs - (List bugs here.)
# Known Bugs - (List known bugs here.)
# Bug 03/07/2023: When entering input for 'name', it accepts numbers and other characters ('!') when it should not.
# Bug 03/07/2023: When entering input for 'phone', it accepts letters and other characters ('!') when it should not.


# IMPORT STATEMENTS found here. ~~~~~~~~~~~~~~
import random # Importing the random module. Provides function for generating random numbers and choosing something random from the selection.
from random import randint # Choosing random integer.


# Constants found here.


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
    print("We are a trusted chat bot that will help you make online orders for BTS albums!")
    print("My name is {}!". format(name)) # The '{}' will be replaced by what we have formatted, 'name', so that it is replaced with a randomly generated name from the list.
    print("I will be here to help you make your online orders!")


# MENU FOR CLICK & COLLECT/DELIVERY. ~~~~~~~~~~~~~~
# Menu for the user to choose either the Click & Collect or Delivery option.
def order_type():
    del_click = "" # This variable is equal to default, empty, blank string.
    # This variable will change to 'clickandcollect' if 1 is entered.
    # This variable will change to 'delivery' if 2 is entered.
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
                    # If Click & Collect is chosen, then the variable, 'del_click', will equal to "clickandcollect".
                    del_click = "clickandcollect" # This will change the 'del_click' variable.
                    clickandcollect_info() # Will run the clickandcollect() function.
                    break
                elif delivery == 2: # Checking if what is entered is '2'.
                    print ("Delivery") # If '2' is entered, 'Delivery' will be printed.
                    # If Delivery is chosen, then the variable, 'del_click', will equal to "delivery".
                    delivery_info() # Will run the delivery() function.
                    del_click = "delivery" # This will change the 'del_click' variable.
                    break # Once the input satisfies this point of the code, the program will break out of this while loop.
            
            # When input is a number that is not 1 or 2, the program will run the else statement.
            else:
                print("The number you enter must be 1 or 2.") # Letting the user know why their input did not work.
        
        # When the user does not enter either '1' or '2', the ValueError will print these error messages.
        except ValueError:
            print("That is not a valid number.")
            print("Please enter 1 or 2.")
    return del_click # This will return the 'del_click' variable back down to the main() function at 'del_click = order_type()'.


# CLICK & COLLECT INFORMATION. ~~~~~~~~~~~~~~
# Question (variable) comes from here.
# Defining the function, 'clickandcollect()' for the click and collect component of the main program.
def clickandcollect_info():
    question = ("Please enter your name. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'name'.
    # Getting the customer details name from the above function, bringing in the question.
    customer_details['name'] = not_blank(question) # Customer name will go to the function for 'not_blank'.
    print(customer_details['name'])


    question = ("Please enter your phone number. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'phone'.
    # Getting the customer details phone from the above function, bringing in the question.
    customer_details['phone'] = not_blank(question) # Customer name will go to the function for 'not_blank'.
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
    customer_details['name'] = not_blank(question) # Customer name will go to the function for 'not_blank'.
    print(customer_details['name'])


    question = ("Please enter your phone number. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'phone'.
    # Getting the customer details phone from the above function, bringing in the question.
    customer_details['phone'] = not_blank(question) # Customer name will go to the function for 'not_blank'.
    print(customer_details['phone'])


    question = ("Please enter your house number. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'house'.
    # Getting the customer details phone from the above function, bringing in the question.
    customer_details['house'] = not_blank(question) # Customer name will go to the function for 'not_blank'.
    print(customer_details['house'])


    question = ("Please enter your street name. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'street'.
    # Getting the customer details phone from the above function, bringing in the question.
    customer_details['street'] = not_blank(question) # Customer name will go to the function for 'not_blank'.
    print(customer_details['street'])


    question = ("Please enter your suburb. ") # Displaying our question.
    # This will go into the customer_details dictionary and it will have a variable name of 'suburb'.
    # Getting the customer details phone from the above function, bringing in the question.
    customer_details['suburb'] = not_blank(question) # Customer name will go to the function for 'not_blank'.
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


    # Starting loop with the 'while' statement. The condition is 'True'.
    while True:
        try: # The try statement will catch and handle except statements.
            # The program asks the user how many albums they want to order with the 'input' statement and takes it in as a string.
            # The 'int' is used to convert the input of the user into an integer.
            # The integer will then be stored to the 'num_albums' variable.
            num_albums = int(input("How many albums do you want to order? "))
            if num_albums >= 1 and num_albums <= 8: # Not accepting anything less than one, not accepting anything greater than 8.
                break # If meets criteria.
            # If the input is less than 1 or greater than 8, the program will run the 'else' statement.
            else:
                print("Your order must be between 1 and 8.")
        # Validation for the input.
        except ValueError:
            print("That is not a valid number.") # Prints if the input is not a number (a letter, a character).
            print("Please enter a number between 1 and 8.") # Prints if the input is a number less than 1 or greater than 8.


    # Choose album from the album list.
    # Used the 'for' statement to create a loop for the number of items that the user has chosen, found in num_albums.
    for item in range(num_albums): # Counting through how many albums have been chosen.
        # Another loop is made with the 'while' statement to ensure that the user can enter their chosen number.
        while num_albums > 0:
            while True:
                try: # The try statement will catch and handle except statements.
                    # The program asks the user how many albums they want to order with the 'input' statement and takes it in as a string.
                    # The 'int' is used to convert the input of the user into an integer.
                    album_ordered = int(input("Please choose the albums you would like to order by entering its corresponding number from the list provided. "))
                    if album_ordered >= 1 and album_ordered <= 15: # Not accepting anything less than one, not accepting anything greater than 15.
                        break # If meets criteria.
                    # If the input is less than 1 or greater than 15, the program will run the 'else' statement.
                    else:
                        print("Your order must be between 1 and 15.")
                # Validation for the input.
                except ValueError:
                    print("That is not a valid number.") # Prints if the input is not a number (a letter, a character).
                    print("Please enter a number between 1 and 15.") # Prints if the input is a number less than 1 or greater than 15.
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
    print("Customer Details") # Letting the user know that was is going to be printed will be their customer details.
    # If the variable, 'del_click' is equal to 'clickandcollect', the following will be printed.
    if del_click == "clickandcollect":
        print("Your Order is for Click and Collect.")
        # Print statement that is used to display to the user the details of their order after being formatted.
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    # If the variable, 'del_click' is equal to 'delivery', the following will be printed.
    elif del_click == "delivery":
        print("Your Order is for Delivery.")
        if len(order_list) >= 5: # Checking if 5 or more albums have been ordered.
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


# Ability to cancel the current order or to proceed with a new order.


# Option to create a new order or to exit out of the program.


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


# Call the main function.
# Since the welcome() function was called within the main() function, then this main() function will
# - execute the welcome() function when called.
main()