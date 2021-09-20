# Exercises


# 1 - Area Calc
import math


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width)/cover)
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# 2 - Prime Numbers
def prime_checker(number):
    division = False
    for num in range(2, number):
        if number % num == 0:
            division = True
    if not division and number != 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)


