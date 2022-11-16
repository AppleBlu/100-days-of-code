# Asking the user for the bill amount
bill = input('How much is the final bill? \nBill: £')
# Asking the user how many people they want to split the bill with
people = input('How many people are you splitting the bill between? \nPeople: ')
# Asking the user how much of a tip they want to give
tip = input('What % tip would you like to give (10, 15, 20 etc.) \nTip: ')


# Dividing the tip up among the people
bill_per_person = (int(bill) / int(people))
# Calculating the tip
tip = float(tip) / 100 * int(bill_per_person)
# Adding the tip to each person's bill
bill_total = bill_per_person + tip
# Rounding the bill to a 2-digit number
round(bill_total)

# Printing the bill per person with the tip
print(f'\nYou should split the bill between {people} people in the amount of £{bill_total}')
