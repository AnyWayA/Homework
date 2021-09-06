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


# 4 - Rock, paper, scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you want to choose? Rock - 0, Paper - 1, Scissors - 2.")
user_num = int(input("It's: "))
computer_num = random.randint(0, 2)

if user_num == 0:
    print("You: " + rock)
    if computer_num == 0:
        print("Computer: " + rock)
        print("Drawn")
    elif computer_num == 1:
        print("Computer: " + paper)
        print("You lose")
    elif computer_num == 2:
        print("Computer: " + scissors)
        print("You win")
elif user_num == 1:
    print("You" + paper)
    if computer_num == 0:
        print("Computer: " + rock)
        print("You win")
    elif computer_num == 1:
        print("Computer: " + paper)
        print("Drawn")
    elif computer_num == 2:
        print("Computer: " + scissors)
        print("You lose")
elif user_num == 2:
    print("You" + scissors)
    if computer_num == 0:
        print("Computer: " + rock)
        print("You lose")
    elif computer_num == 1:
        print("Computer: " + paper)
        print("You win")
    elif computer_num == 2:
        print("Computer: " + scissors)
        print("Drawn")