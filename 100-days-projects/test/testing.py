with open(file="test_file.txt", mode="r") as data:
    data_contents = data.read()

with open(file="test_file.txt", mode="w") as data:
    data.write("hello world")


