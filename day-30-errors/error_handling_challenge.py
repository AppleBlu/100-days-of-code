# Bugged code
pass
"""fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


make_pie(4)"""

# Fixed code
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error:
        print(f'Fruit Pie. {error}')
    else:
        print(fruit + " pie")


make_pie(3)
