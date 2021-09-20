# Exercises


# 1 - Heads or Tails (random)
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

number = random.randint(0, 1)
print("Number = " + str(number))

if number == 0:
    print("Tails")
elif number == 1:
    print("Heads")


# 2 - Who's Paying
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)

# print(random.choice(names))

index_person = random.randint(1, len(names)) - 1
print(f"{names[index_person]} should pay")


# 3 - Treasure_map
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? RowColumn ")

row = int(position[0]) - 1
column = int(position[1]) - 1

treasure_map[row][column] = "X   "
print(f"{row1}\n{row2}\n{row3}")
