import random
import hangman_art
import hangman_words

word = random.choice(hangman_words.word_list)
end_of_game = False
lives = 6

# Create blanks.
all_attempts = []

display = []
for letters in word:
    display.append("_")


# Game code.
print(hangman_art.logo)
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # if letter has already been.
    if guess in all_attempts:
        print("This letter has already been!")

    # if letter in the word.
    elif guess in word:
        for index in range(len(word)):
            if word[index] == guess:
                display[index] = guess
        print("Nice!")

    # if letter NOT in the word.
    elif guess not in word:
        lives -= 1
        print("Oops, wrong. It's not in the word")
        print(hangman_art.stages[lives])

    all_attempts.append(guess)

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if the game should end.
    if "_" not in display:
        end_of_game = True
        print("You win!")
    if lives == 0:
        end_of_game = True
        print("You lose!\nThe word was: " + word)

