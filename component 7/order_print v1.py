# LIST OF STORED ORDERED ALBUMS. ~~~~~~~~~~~~~~
order_list = ['2 Cool 4 Skool','O!RUL8,2?','Skool Luv Affair','No More Dream']

# LIST OF STORED ALBUM PRICES. ~~~~~~~~~~~~~~
order_cost = [25.70, 32.20, 28.40, 40.20]


count = 0 # 25.70 is at the position of 0.
# The 'for' statement will create a loop that will go through each item in the 'order_list'.
for item in order_list:
    print("Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count])) # Will print the formatted albums ordered and their corresponding price.
    # The 'count' variable keeps track of the correct index in the 'order_cost' list.
    count = count+1 # Adding 1 to the 'count' variable so that next time, when the function picks out a different item, it will become a different number.