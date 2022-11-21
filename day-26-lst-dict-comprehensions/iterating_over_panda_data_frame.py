import pandas

student_dict = {
    'student': ['Tom', 'Sinead', 'Mati', 'Ben', 'Ethan'],
    'score': [10, 23, 17, 24, 22]
}

# Looping through dicts
for (key, value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

"""Loop through data frame
for (key, value) in student_data_frame.items():
    print(value)"""

# Loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
    if row.student == 'Tom':
        print(f'Toms score is: {row.score}')
