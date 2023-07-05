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


# Making sure that the input is a valid string.
# Setting up the variable, 'question'.
question = "Please enter your name. " # The 'question' variable is a parameter. It is used in the function, 'check_string()'.


# Setting up the variable, 'name'.
name = check_string(question)
# The 'name' variable will get the result of the function.

# Print out the name, the valid input, to make sure it is working.
print(name)