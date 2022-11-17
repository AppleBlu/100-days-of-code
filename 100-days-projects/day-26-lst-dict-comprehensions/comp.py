numbers = [1, 2, 3]
# How we would add 1 to each number in the list above using a for loop
new_list = []
for num in numbers:
    num_plus_1 = num + 1
    new_list.append(num_plus_1)

"""How we would do the same but in one line using comprehension

new_list = [new_item for item in items]

list var        new_item  each num in list numbers"""
new_list_comp = [num + 1 for num in numbers]

new_list_comp2 = [num + 1 for num in range(1, 4)]

# List of names
names = ['Tom', ' Ben', 'Sinead', 'Gary']
# Getting all names that are less than 5 chars and converts them to upper case
short_names = [name.upper() for name in names if len(name) < 5]
