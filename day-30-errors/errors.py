# File not found
pass
"""with open('a_file') as file:
        file.read()"""

# KeyError
"""a_dictionary = {'key': 'value'}
   a_value = a_dictionary['non_existent_key']"""

# IndexError
"""fruit_list = ['apple', 'banana', 'pear']
   fruit = fruit_list[3]"""

# TypeError
"""text = 'abc'
   print(text + 1)"""

# Exception keywords
"""try: ~ Try something that might cause and exception
   except: ~ Do this if there was an exception
   else: ~ Do this if there where no exceptions
   finally: ~ Do this no matter what happens"""

# Examples
"""
try:
    file = open('a_file.txt') ~ Cant find the file
    a_dictionary = {'key': 'value'}
    print(a_dictionary['adadsfds'] ~ Cant find the key
    
except FileNotFoundError: ~ Looks for a specific error
    print('There was an error')
    print('New file created')
    file = open(a_file.txt, 'w') ~ Makes the file since it does not exist
    
except KeyError as error_message: ~ Looks for a specific error and saves the error to a variable
    print(f'That key: {error_message} does not exist')
    
else: ~ Only executes if there are no errors
    content = file.read()
    print(content)

finally: ~ No matter what happens the file will close
    file.close()
    print('File was closed')
    raise TypeError('This is an error i made up') ~ crashes the code with an error"""

# Example
height = float(input('height: ')) # in meters
weight = float(input('weight: '))
if height > 3:
    raise ValueError('Human height should not be over 3 meters.')

bmi = weight / height ** 2
print(bmi)
