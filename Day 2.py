# Exercises


# 1 - the sum of the numbers
two_digit_number = input("Type a two digit number: ")

number1 = two_digit_number[0]
number2 = two_digit_number[1]
answer = int(number1) + int(number2)
print("The sum of the numbers is " + str(answer))


# 2 - BMI calculation
weight = input("enter your weight in kg: ")
height = input("enter your height in m: ")

bmi = int(float(weight) // (float(height) ** 2))
print("Your BMI is " + str(bmi))


# 3 - How many time you have in your life?
age = int(input("What is your current age?\n"))

# Constants
life = 90
days_a_year = 365
weeks_a_year = 52
months_a_year = 12

# All time you have
life_days = days_a_year * (life - age)
life_weeks = weeks_a_year * (life - age)
life_months = months_a_year * (life - age)

print(f"You have {life_days} days, and {life_weeks} weeks, and {life_months} months")


# 4 - To split the bill (with tip)
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = bill * percentage_tip/100
bill_with_tip = bill + tip
to_split = round(bill_with_tip / people, 2)

print(f"Each person should pay: $ {to_split}")
