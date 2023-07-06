def check_phone(ph_low, ph_high, question):
    # Bringing in the variable, 'question', into the function.
    # Bringing in the variable, 'ph_low', for 8, into the function.
    # Bringing in the variable, 'ph_high', for 11, into the function.
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
            if count >= ph_low and count <= ph_high:
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


# The pohone numbers in New Zealand are generally 8 to 11 digits long.
# The program should check if the phone number being entered is only ranging and including from 8 to 11 digits long.
# Setting the variables.
# These are parameters, they are used in the function, 'check_phone()'.
ph_low = 8 # Lowest amount of digits allowed to be entered.
ph_high = 11 # Highest amount of digits allowed to be entered.


# Making sure that the input is a valid phone number.
# Setting up the variable, 'question'.
question = "Please enter your phone number. " # The 'question' variable is a parameter. It is used in the function, 'check_phone()'.


# Setting up the variable, 'phone'.
phone = check_phone(ph_low, ph_high, question) # When entering the phone  number input for the variable, 'phone', it will be checked by the function to make sure that the input is all numbers.
# Providing these paramters to the 'phone' variable.


# Checking that it works properly.
print(phone)