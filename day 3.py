# Exercises


# 1 - Even or Odd
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print(f"Your number {number} is Even")
else:
    print(f"Your number {number} is Odd")

# 2 - The interpretation of the BMI (if/else)
weight = input("enter your weight in kg: ")
height = input("enter your height in m: ")

bmi = float(weight) // (float(height) ** 2)
print("Your BMI is " + str(int(bmi)))

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Slightly overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinically obese")

# 3 - Leap/not leap
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is LEAP")
    elif year % 400 == 0:
        print(f"{year} is LEAP")
    else:
        print(f"{year} is NOT LEAP")
else:
    print(f"{year} is NOT LEAP")

# 4 - Pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1

print("Your final bill is $" + str(bill))

# 5 - The Love Calculator
print("Welcome to the Love Calculator!")
name1_not_lower = input("What is your name? \n")
name2_not_lower = input("What is their name? \n")

name1 = name1_not_lower.lower()
name2 = name2_not_lower.lower()
name_string = name1 + name2

t = name_string.count("t")
r = name_string.count("r")
u = name_string.count("u")
e = name_string.count("u")
true_word = t + r + u + e

l_letter = name_string.count("l")
o = name_string.count("o")
v = name_string.count("v")
love_word = l_letter + o + v + e

true_love = str(true_word) + str(love_word)

print("Your love score = " + true_love)

true_love = int(true_love)
# if (true_love < 10) or (true_love > 90):
if 10 < true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif 40 < true_love < 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}")


# 6 - Игра по сценарию
print("""
                         .-. .-.
                        (   |   )
                      .-.:  |  ;,-.
                     (_ __`.|.'_ __)
                     (    ./Y\.    )
                      `-.-' | `-.-'
                            |
                            | 
""")
print("Добро пожаловать в игру по спасению жизни!\n"
      "Так уж вышло, что те ягоды, которые ты посчитал безопасными, оказались редким ведьминым ядом. \n"
      "И теперь, чтобы спасти свою жизнь, ты должен добраться до горы Гарибальди, где растет редчайший белый клевер,\n"
      "являющийся противоядием сильнейших ядов. \nПуть туда не прост, будь осторожен!")
print()

trail = input("Итак, ты на распутье. Перед тобой две тропы: одна ведет в тихий лес, другая через маковое поле. \n"
              "Куда пойдешь? Лес/Поле\n")
if trail.lower() == "лес":
    lake = input("Отличное решение! Лес оказался небольшим, и вот ты уже стоишь перед озером в какой-то глуши.\n"
                 "Голова слегка кружится от яда, но ты видишь совсем новенькую лодку и деревянный мост. \n"
                 "Как одолеешь озеро? Лодка/Мост\n")
    if lake.lower() == "мост":
        mountains = input("Верно! Ты пересек хрупкий мост и перед тобой три горы: Зеленая, Белая и Красная. \n"
                          "От яда тебя уже обдает жар, на какую гору полезешь? З/Б/К\n")
        if mountains.lower() == "б":
            clover = input(
                "Конечно! Гора белая из-за клевера, что мы ищем! Тут есть трехлистный и четырехлистный клевер. \n"
                "Какой съешь? 3/4/Любой\n")
            if clover.lower() == "3":
                print("Ура, победа! Клевер дал нужное противоядие, но ты конечно кринж. Не ешь больше что попало! :)")
            elif clover.lower() == "любой":
                print("Даже эльфы офигели от твоего пофигизма! И отобрали у тебя четырехлистник, \n"
                      "чтоб ты не умер от своей же глупости. Себастьян отсюда :)")
            else:
                print("Что за стереотипы? Четырехлистный клевер - счастливый? \nРядом эльфы смеются над тобой. \n"
                      "Они просто приделали трехлистникам ядовитый листочек, а ты купился. Все хорошо, ты умер!")
        elif mountains.lower() == "к":
            print("Ой, оказывается жар у тебя не от яда, а от лавы, стекающей по горе, которую ты выбрал. \n"
                  "Жаль, ты умер! Но был так близко!")
        else:
            print("Почему зеленая? Потому что клевер зеленый? А ничего, что мы ищем белый клевер, а? Ты умер, позор!")
    else:
        print("У тебя галлюцинации? Какая новая лодка в глуши? Она вообще вся в дырах. \n"
              "Ты и до середины-то не доплыл. Смерть.")
else:
    print("Ну да, умер на первом же вопросе. Леса испугался? А полное поле наркотиков норм? \n"
          "Отлично, наркоман фигов. Ты умер в блаженном сне!")
