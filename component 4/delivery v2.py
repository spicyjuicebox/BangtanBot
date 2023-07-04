# Customer Details Dictionary
# Curly brackets indicate a dictionary (stores information - customer details). Holds information, better than a list.
customer_details = {}


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


def delivery():
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

delivery()