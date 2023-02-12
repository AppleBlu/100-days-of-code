
# Opening a text file in write mode and changing the txt inside
with open(file='my_file.txt', mode='w') as file:
    file.write('New text.')

# Opening a text file using an absolute path in write mode and changing the txt inside
# If I was using relative path "../../../Desktop/my_file.txt"
with open(file='/100-Days/day-24-files/my_file.txt', mode='w') as file:
    file.write('New text.')

# Opening a txt file and appending to the end of the file
with open(file='my_file.txt', mode='a') as file:
    file.write(' New text')

# Opening a txt file, reading it and printing it
with open(file='my_file.txt') as file:
    contents = file.read()
    print(contents)

# Creating a new file
with open(file='new_file.txt', mode='w') as new_file:
    new_file.write('hello')

# Opening a txt file, reading it and printing it
with open(file='new_file.txt') as new_file:
    contents = new_file.read()
    print(contents)
