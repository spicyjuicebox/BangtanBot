# Defines the 'sys' function class for the 'sys.exit' so that it exits the program.
import sys

# List of stored ordered pizzas.
order_list = []

# List of stored pizza prices.
order_cost = []

# Customer Details Dictionary.
customer_details = {}


# Asking the user if they want to start another order or to exit the Bangtan Bot program.
print ("Do you want to start another Order or Exit?")
print ("To start another order, please enter 1.") # Input of 1 will make another order.
print ("To exit the BOT, please enter 2.") # Input of 2 will exit the Bangtan Bot program.
while True:
    try:
        confirm = int(input("Please enter a number. ")) # The input, 1 or 2, will be equal to 'confirm'.
        if confirm >= 1 and confirm <= 2: # Checking if the input is only 1 or 2.
            if confirm == 1: # If 'confirm' is equal to 1, a new order will be made.
                print ("New Order") # Letting the user know that a new order will be made.
                # Clearing the data from the current order from all lists.
                order_list.clear() # Clearing data from the list, 'order_list'.
                order_cost.clear() # Clearing data from the list, 'order_cost'.
                customer_details.clear() # Clearing data from the list, 'customer_details'.
                break # Breaking out of the loop.

            elif confirm == 2: # If 'confirm' is equal to 2, the program will stop.
                print ("Exit") # Letting the user know that they will now exit out of the Bangtan Bot program.
                order_list.clear() # Clearing data from the list, 'order_list'.
                order_cost.clear() # Clearing data from the list, 'order_cost'.
                customer_details.clear() # Clearing data from the list, 'customer_details'.
                sys.exit() # Exiting out of the program.
                break # Breaking out of the loop.
        # When input is a number that is not 1 or 2.
        else:
            print("The number must be 1 or 2.")
    
    # When the input is a letter (not a number).
    except ValueError:
        print("That is not a valid number.")
        print("Please enter 1 or 2. ")


def main():
    print("Start again.")