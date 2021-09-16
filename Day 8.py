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


# 3 - Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, code_direction):
    code_text = ""
    if code_direction == "decode":
        shift_amount *= -1
    # comment 1
    for letter in plain_text:
        if letter not in alphabet:
            code_text += letter
        else:
            letter_position = alphabet.index(letter)
            new_letter_position = letter_position + shift_amount
            code_text += alphabet[new_letter_position]

    print(code_text)


caesar_coding = "yes"
while caesar_coding == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    # comment 2
    caesar(plain_text=text, shift_amount=shift, code_direction=direction)
    caesar_coding = input("Do you wanna continue? yes/no\n").lower()


# COMMENTS
# comment 1 - логика по выбору направления кодировки:
# if code_direction == "encode":
#     new_letter_position = letter_position + shift_amount
# else:
#     new_letter_position = letter_position - shift_amount

# comment 2 - недопуск слишком большого сдвига:
#
# if shift > len(alphabet)/2:
#     print("The number is too big! Need to be < 27")
# else:
#     caesar(plain_text=text, shift_amount=shift, code_direction=direction)


# OPTIONS
# option 1 - encode с циклами:
# def encrypt(plain_text, shift_amount):
#     text_list = list(plain_text)
#     for i in range(len(text_list)):
#         x = 0
#         done = False
#         while not done:
#             if text_list[i] == alphabet[x]:
#                 text_list[i] = alphabet[x+shift_amount]
#                 done = True
#             else:
#                 x += 1
#     print(f"{''.join(text_list)}")

# option 2 - encode с универсальным циклом для любого значения shift:
# def encrypt(plain_text, shift_amount):
# encode_text = ""
# for letter in plain_text:
#     letter_position = alphabet.index(letter)
#     new_letter_position = letter_position + shift_amount
#     encode_text += alphabet[new_letter_position]
# if new_letter_position >= len(alphabet):
#     second_letter_position = new_letter_position - len(alphabet)
#     while second_letter_position >= len(alphabet):
#         second_letter_position -= len(alphabet)
#     encode_text += alphabet[second_letter_position]
# else:
#     encode_text += alphabet[new_letter_position]
# print(encode_text)
