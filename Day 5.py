# Exercises


# 1 - Average Height
student_heights = input("Input a list of student heights ").split()
for i in range(0, len(student_heights)):
  student_heights[i] = int(student_heights[i])

# without len() and sum()
quantity_heights = 0
for q in student_heights:
    quantity_heights += 1

sum_heights = 0
for s in range(0, quantity_heights):
    sum_heights += student_heights[s]

average_height = sum_heights//quantity_heights
print(f"Average height = {average_height}")


# 2 - Highest Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")


# 3 - Adding Evens
total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(total)


# 4 - FizzBuzz
for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# 5 - Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for letter in range(0, nr_letters):
    password += random.choice(letters)
for symbol in range(0, nr_symbols):
    password += random.choice(symbols)
for number in range(0, nr_numbers):
    password += random.choice(numbers)
print(password)

# hard level

password_list = []
for x in password:
    password_list.append(x)
# random.shuffle(password_list)

for i in range(0, 55):
    a = random.randint(0, len(password_list)-1)
    b = random.randint(0, len(password_list)-1)
    c = password_list[a]
    password_list[a] = password_list[b]
    password_list[b] = c

random_password = ""
for p in password_list:
    random_password += p
print(random_password)
