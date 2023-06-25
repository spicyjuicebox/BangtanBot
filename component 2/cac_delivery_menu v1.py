# Menu for the user to choose either the Click & Collect or Delivery option.
# Print statement that asks the user whether they want their order to be for Click & Collect or Delivery.
print ("Do you want your order to be CLICK & COLLECT or DELIVERED to you?")

# Print Statement asking the user to enter d for Delivery, or c for Click & Collect.
print ("For DELIVERY, enter d. For CLICK & COLLECT, enter c.")

# Managing the Delivery.
# Whatever is entered in the input will be assigned to the variable of 'delivery'.
delivery = input()

if delivery == "d": # Checking if what is entered is 'd'.
    print("Delivery") # If 'd' is entered, 'Delivery' will be printed.

elif delivery == "c": # Checking if what is entered is 'c'.
    print("Click & Collect") # If 'c' is entered, 'Click & Collect' will be printed.