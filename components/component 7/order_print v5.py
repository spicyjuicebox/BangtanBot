# LIST OF STORED ORDERED ALBUMS. ~~~~~~~~~~~~~~
order_list = ['2 Cool 4 Skool','O!RUL8,2?','Skool Luv Affair','No More Dream']

# LIST OF STORED ALBUM PRICES. ~~~~~~~~~~~~~~
order_cost = [25.70, 32.20, 28.40, 40.20]


# Customer Details Dictionary
# Curly brackets indicate a dictionary (stores information - customer details). Holds information, better than a list.
customer_details = {'name': 'Mark','phone': '88','house': '45','street': 'Harry', 'suburb': 'Howick'}


# Defining the function, 'print_order()'.
def print_order():
    total_cost = sum(order_cost)
    print("Customer Details") # Letting the user know that was is going to be printed will be their customer details.
    # Print statement that is used to display to the user the details of their order after being formatted.
    print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} \nCustomer Street: {customer_details['street']} \nCustomer Suburb: {customer_details['suburb']}")
    # The 'f' at the front is a way to format.
    # For the 'Customer Name' in {customer_details['name']}, it will have the inserted value of the 'name' key from the 'customer_details' dictionary list.
    # For the 'Customer Phone' in {customer_details['phone']}, it will have the inserted value of the 'phone' key from the 'customer_details' dictionary list.
    # For the 'Customer Address' in {customer_details['house']}, it will have the inserted value of the 'house' key from the 'customer_details' dictionary list.
    # For the 'Customer Street' in {customer_details['street']}, it will have the inserted value of the 'street' key from the 'customer_details' dictionary list.
    # For the 'Customer Suburb' in {customer_details['suburb']}, it will have the inserted value of the 'suburb' key from the 'customer_details' dictionary list.
    print()
    print("Order Details") # Letting the user know that was is going to be printed will be their order details.
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

# Calling the print_order() function to check if it is working properly.
print_order()