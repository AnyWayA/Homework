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