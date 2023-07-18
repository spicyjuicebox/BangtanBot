# LIST OF STORED ORDERED ALBUMS. ~~~~~~~~~~~~~~
order_list = ['2 Cool 4 Skool','O!RUL8,2?','Skool Luv Affair','No More Dream']

# LIST OF STORED ALBUM PRICES. ~~~~~~~~~~~~~~
order_cost = [25.70, 32.20, 28.40, 40.20]


# Customer Details Dictionary
# Curly brackets indicate a dictionary (stores information - customer details). Holds information, better than a list.
customer_details = {'name': 'Mark','phone': '88','house': '45','street': 'Harry', 'suburb': 'Howick'}

# Testing.
#print("\n",customer_details['name'],"\n",customer_details['phone'],"\n",customer_details['house'],"\n",customer_details['street'],"\n",customer_details['suburb'])

# Print statement that is used to display to the user the details of their order after being formatted.
print("Customer Name: {} \nCustomer Phone: {} \nCustomer House Number: {} \nCustomer Street Name: {} \nCustomer Suburb: {}" .format( customer_details['name'],customer_details['phone'],customer_details['house'],customer_details['street'],customer_details['suburb']))
# 'Customer Name: {}' will have the inserted value of the 'name' key from the 'customer_details' dictionary list.
# 'Customer Phone: {}' will have the inserted value of the 'phone' key.
# 'Customer House Number: {}' will have the inserted value of the 'house' key.
# 'Customer Street Name: {}' will have the inserted value of the 'street' key.
# 'Customer Suburb: {}' will have the inserted value of the 'suburb' key.


count = 0 # 25.70 is at the position of 0.
# The 'for' statement will create a loop that will go through each item in the 'order_list'.
for item in order_list:
    print("Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count])) # Will print the formatted albums ordered and their corresponding price.
    # The 'count' variable keeps track of the correct index in the 'order_cost' list.
    count = count+1 # Adding 1 to the 'count' variable so that next time, when the function picks out a different item, it will become a different number.