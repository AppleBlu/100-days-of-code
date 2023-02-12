import random

"""Dictionary comprehensions
Dict comp using a list to build the dict
new_dict = {new_key: new_value for item in list}

Dict comp using a dict to build the dict
new_dict2 = {new_key: new_value for (key, value) in dict.items()}

Dict comp using a dict to build a dict with an if test
new_dict3 = {new_key: new_value for (key, value) in dict.items() if test}"""

# List of names
names = ['Tom', ' Ben', 'Sinead', 'Gary']

# Creating a dictionary with names and a random score
students_scores = {name: random.randint(1, 100) for name in names}

# Creating a dict with students_scores that passed
passed_students = {key: value for (key, value) in students_scores.items() if value >= 60}

print(students_scores)
print(passed_students)
