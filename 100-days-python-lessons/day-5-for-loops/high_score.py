student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for number in student_scores:
    if number > highest_score:
        highest_score = number

print(f'The highest score in the class is: {highest_score}')
