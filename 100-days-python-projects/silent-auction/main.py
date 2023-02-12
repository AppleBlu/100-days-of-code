# Importing files
import art

# Printing the logo art
print(art.logo)

# Empty dictionary
name_to_bid = {}


# Function that is called to run the application
def bid_app():
    """Will run the application"""
    # Asking the user for their name and bid
    name = input('\nWhats your name? \nName: ')
    bid = float(input('Enter your bid \nBid: £'))

    # Adding the inputs to the dict name_to_bid
    name_to_bid[name] = bid

    # Function to ask the user if everyone has bid
    def more_bidders_question():
        """Will ask the bidder if anyone else would like to bid and dependent on their answer it will restart the app
        or print the highest bidder """
        more_bidders = input('Is there anyone else that would like to bid (Y/N) : ').lower()

        # If statement that checks if the user entered 'y'
        if more_bidders == 'y':

            # Prints multiple new lines, so you cant see the last persons bid
            print('\n' * 50)
            # Calling the application
            bid_app()

        # Checks if the user entered 'n'
        elif more_bidders == 'n':

            # New list
            highest_bidder = ['', 0]

            # For loop to add the highest bidder and bid to highest_bidder list
            for person in name_to_bid:
                persons_bid = name_to_bid[person]
                if persons_bid > highest_bidder[1]:
                    highest_bidder[1] = persons_bid
                    highest_bidder[0] = person

            # Printing the display
            print(f'The highest bidder is {highest_bidder[0]} with a bid of £{highest_bidder[1]}')

        # Checks if the user entered an invalid input and asks them again if they did
        else:
            print('Invalid input')
            more_bidders_question()

    # Calling function
    more_bidders_question()


# Calling the application function
bid_app()
