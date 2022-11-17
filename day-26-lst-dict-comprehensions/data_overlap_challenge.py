# Challenge 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in numbers if num % 2 == 0]

print(result)

# Challenge 2 (make a list with all numbers in both files)
with open(file='file1.txt') as file1:
    file_1_contents = file1.readlines()

with open(file='file2.txt') as file2:
    file_2_contents = file2.readlines()


result_2 = [int(num) for num in file_1_contents if num in file_2_contents]


print(result_2)
