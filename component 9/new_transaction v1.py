# Asking the user if they want to start another order or to exit the Bangtan Bot program.
print ("Do you want to start another Order or Exit?")
print ("To start another order, please enter 1.") # Input of 1 will make another order.
print ("To exit the BOT, please enter 2.") # Input of 2 will exit the Bangtan Bot program.
while True:
    try:
        confirm = int(input("Please enter a number. ")) # The input, 1 or 2, will be equal to 'confirm'.
        if confirm >= 1 and confirm <= 2: # Checking if the input is only 1 or 2.
            if confirm == 1: # If 'confirm' is equal to 1, a new order will be made.
                print ("New Order")
                break # Breaking out of the loop.

            elif confirm == 2: # If 'confirm' is equal to 2, the program will stop.
                print ("Exit")
                break # Breaking out of the loop.
        # When input is a number that is not 1 or 2.
        else:
            print("The number must be 1 or 2.")
    
    # When the input is a letter (not a number).
    except ValueError:
        print("That is not a valid number.")
        print("Please enter 1 or 2. ")