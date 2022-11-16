import math


def paint_calc(height, width, cover):
    num_of_cans = (height * width) / cover
    num_of_cans_rounded = math.ceil(num_of_cans)
    print(f'You\'ll need {num_of_cans_rounded} cans of paint.')


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
