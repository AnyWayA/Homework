# Exercises


# 1 - debug print()

# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the"+" sign.")
#  print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
print()


# 2 - input() and letter counter
name = input("Write your Name: ")

# letter_counter = 0
# for i in range(len(name)):
#     letter_counter += 1
# print("The word '" + name + "' has " + str(letter_counter) +

print("The word '" + name + "' has " + str(len(name)) + " letters!")
print("Result: " + str(len(input("Name, again: "))))


# 3 - change the value of variables
a = input("a: ")
b = input("b: ")

# c = a
# a = b
# b = c

a_new = b
b_new = a
a = a_new
b = b_new

print("a: " + a)
print("b: " + b)


# 4 - Bang Name Generator
print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)
