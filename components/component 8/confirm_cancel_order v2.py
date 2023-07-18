# The CONFIRM or CANCEL order options.
print ("Please confirm your order.")
print ("To CONFIRM, please enter 1.") # Letting the user know that entering 1 will CONFIRM their order.
print ("To CANCEL, please enter 2.") # Letting the user know that entering 2 will CANCEL their order.
while True:
    try:
        confirm = int(input("Please enter the number 1 or 2. ")) # The input, 1 or 2, will be equal to 'confirm'.
        if confirm >= 1 and confirm <= 2: # Checking if the input is only 1 or 2.
            if confirm == 1: # If 'confirm' is equal to 1, the order is confirmed.
                # Letting the user know that the order has been confirmed.
                print("Your Order has been Confirmed.")
                print("Order Confirmed. You will receive a text message shortly to know when your order is ready to click and collect.")
                print("You will soon receive text messages to notify you of the status of your delivery.")
                break # Breaking out of the loop.

            elif confirm == 2: # If 'confirm' is equal to 2, the order is cancelled.
                # Letting the user know that the order has been cancelled.
                print("Your Order has been Cancelled.")
                print("You can restart your order or exit the Bangtan Bot.")
                break # Breaking out of the loop.
        # When input is a number that is not 1 or 2.
        else:
            print("The number must be 1 or 2.")
    
    # When the input is a letter (not a number).
    except ValueError:
        print("That is not a valid number.")
        print("Please enter 1 or 2. ")