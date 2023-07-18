# Customer Details Dictionary
# Curly brackets indicate a dictionary (stores information - customer details). Holds information, better than a list.
customer_details = {}


# Basic Instructions
# Print statement letting the user know that they have to enter in their personal details next.
print("Please enter your customer information for your Click and Collect order.")


# Customer Name and Not Blank
# What the user enters in this input line of code will be assigned to the variable, 'name'.
# Assigning the value, 'False', to the variable, 'valid'.
# By assigning it this way, it is indicated that the condition for the valid variable is not satisfied.
# It is used to track the values being entered by the user into the program and will control the flow of the program.
valid = False
# Starting a while loop as long as the condition is 'not valid'.
while not valid:
    # This will go into the customer_details dictionary and it will have a variable name of 'name'.
    customer_details['name'] = input("Please enter your name. ") # The input will be sent to the customer_details dictionary, with the variable of 'name'.
    if customer_details['name'] != "": # Checking if the input is blank.
        print (customer_details['name']) # Program will print the value that is assigned to the variable 'name', found in the 'customer_details' dictionary.
        # Use break to get out of the loop.
        break
    # When the condition for the 'if' statement is false, the program will skip to the 'else' code.
    else:
        # The 'else' statement will print this line of code.
        print("Sorry, this cannot be blank.") # The program lets the user know that what they enter cannot be blank.
        # No break so it will continue to go into a loop until the user enters the correct input.


# Customer Phone Number and Not Blank
# What the user enters in this input line of code will be assigned to the variable, 'phone'.
# Assigning the value, 'False', to the variable, 'valid'.
# By assigning it this way, it is indicated that the condition for the valid variable is not satisfied.
# It is used to track the values being entered by the user into the program and will control the flow of the program.
valid = False
# Starting a while loop as long as the condition is 'not valid'.
while not valid:
    # This will go into the customer_details dictionary and it will have a variable name of 'phone'.
    customer_details['phone'] = input("Please enter your phone number. ")  # The input will be sent to the customer_details dictionary, with the variable of 'phone'.
    if customer_details['phone'] != "": # Checking if the input is blank.
        print (customer_details['phone']) # Program will print the value that is assigned to the variable 'phone', found in the 'customer_details' dictionary.
        # Use break to get out of the loop.
        break
    # When the condition for the 'if' statement is false, the program will skip to the 'else' code.
    else:
        # The 'else' statement will print this line of code.
        print("Sorry, this cannot be blank.") # The program lets the user know that what they enter cannot be blank.
        # No break so it will continue to go into a loop until the user enters the correct input.


print (customer_details)