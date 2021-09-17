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



