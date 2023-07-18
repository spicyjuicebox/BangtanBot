# This is a list that is named, 'album_names'. This list stores the information of the list of albums that the program will be selling.
# The list is defined using the square brackets, '[]'. Inside these are strings that are separated by commas and are enclosed by single quotes to indicate that each are strings.
# The order of the items in this list will be written out in the same order when printed.
album_names = ['2 Cool 4 Skool','O!RUL8,2?','Skool Luv Affair','No More Dream','The Most Beautiful Moment In Life Pt.1','The Most Beautiful Moment In Life Pt.2','The Most Beautiful Moment In Life: Young Forever','WINGS','Love Yourself: Her','Love Yourself: Tear','Love Yourself: Answer','Map of the Soul: Persona','Map of the Soul: 7','BE','Butter']
# The 2 Cool 4 Skool album is at position 0.

# Another list variable that is named, 'album_prices'.
# The list is defined using the square brackets, '[]'. Inside these are strings that are separated by commas and each represent the price of each of the albums to be sold.
# The order of the prices or numbers in this list will be written out in the same order when printed and aligns itself with the album_names list.
album_prices = [25.70, 32.20, 28.40, 40.20, 40.10, 45.70, 62.50, 45.80, 50.50, 58.40, 60.80, 52.20, 90.50, 55.50, 40.20]
# The first 25.70 is at position 0.
# This lines up with the album_names of '2 Cool 4 Skool' with it being at position 0.

# List of stored ordered albums.
order_list = []

# List of stored pizza prices.
order_cost = []

# List to store order cost.

# Bringing in the albums() function from the previous component.
# Defining the function for the albums as albums().
# This function will be responsible for displaying the album names, album prices and their corresponding index numbers.
def albums():
    # Making a variable (Will count through 15 times).
    number_albums = 15 # This is the total number of albums that the bot will be selling.

    # The 'for' statement will create a loop that will start from 0 and will range through to the end of 'number_albums - 1' (from 0 to 14).
    for count in range (number_albums): # Taking 0.
        print("{} {} ${:.2f}" .format(count+1, album_names[count],album_prices[count])) # Prints out each of the album names and album prices by its integer.
        # The {:.2f} rounds them up into 2 decimal places or 2 floats. The 0 appears now.
        # The count+1 will change the 2 Cool 4 Skool position from 0 to 1.
        # The album_names[count] will retrieve the name of the album at the current index, 'count', from the 'album_names' list.
        # The album_prices[count] will retrieve the price of the album at the current index, 'count', from the 'album_prices' list.
        # The output will be printed out through the format, "{album_number} {album_name} ${album_price}".

# Calling the menu() function to check if the album_list component is working properly.
albums()


# Ask for total number of albums for order.
num_albums = 0 # This variable has the value of 0.

# The program asks the user how many albums they want to order with the 'input' statement and takes it in as a string.
# The 'int' is used to convert the input of the user into an integer.
# The integer will then be stored to the 'num_albums' variable.
num_albums = int(input("How many albums do you want to order? "))

# Prints out the value of the 'num_albums' variable after the user had entered in their chosen amount.
print(num_albums)


# Choose album from the album list.
print("Please choose the albums you would like to order by entering its corresponding number from the list provided. ")
# Used the 'for' statement to create a loop for the number of items that the user has chosen, found in num_albums.
for item in range(num_albums): # Counting through how many albums have been chosen.
    # Another loop is made with the 'while' statement to ensure that the user can enter their chosen number.
    while num_albums > 0:
        album_ordered = int(input()) # Choosing number of albums from the album list. The input is taken as an integer.
        order_list.append(album_names[album_ordered]) # Picking out the album name from 'album_names' and is entered into the 'order_list'.
        order_cost.append(album_prices[album_ordered]) # Picking out the album price from 'album_prices' and is entered into the 'order_cost'.
        num_albums = num_albums-1 # Ordered the first album, going back to order the rest of them, taking 1 off that total.

print(order_list)
print(order_cost)