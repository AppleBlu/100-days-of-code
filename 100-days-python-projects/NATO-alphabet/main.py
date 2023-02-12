import pandas

# Examples
"""student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}"""

"""Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}"""

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_frame = pandas.DataFrame(data)

nato_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
incorrect_input = True
while incorrect_input:
    user_input = input('\nEnter A Word: ').upper()
    try:
        nato_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print('\nPlease enter a letters from the alphabet.')
    else:
        print(f'\n{nato_list}')
