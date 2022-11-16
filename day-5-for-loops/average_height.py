student_heights = input("Input a list of student heights ").split()

for height in range(0, len(student_heights)):
    student_heights[height] = int(student_heights[height])

total_height = 0
for height in student_heights:
    total_height += height

number_of_students = 0
for num in student_heights:
    number_of_students += 1

avg_height = round(total_height / number_of_students)

print(avg_height)


