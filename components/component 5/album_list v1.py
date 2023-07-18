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


# Defining the function for the menu as menu().
# This function will be responsible for displaying the album names, album prices and their corresponding index numbers.
def menu():
    # Making a variable (Will count through 15 times).
    number_albums = 15 # This is the total number of albums that the bot will be selling.

    # The 'for' statement will create a loop that will start from 0 and will range through to the end of 'number_albums - 1' (from 0 to 14).
    for count in range (number_albums): # Taking 0.
        print(count, album_names[count],album_prices[count]) # Prints out each of the album names and album prices by its integer.
        # The album_names[count] will retrieve the name of the album at the current index, 'count', from the 'album_names' list.
        # The album_prices[count] will retrieve the price of the album at the current index, 'count', from the 'album_prices' list.

# Calling the menu() function to check if the album_list component is working properly.
menu()