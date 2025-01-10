# Hangman game in python
import random
import os

answers = ("apple", "banana", "orange", "grapes", "gauva", "mango")

# dictionary of key :()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}


def display_hangman(incorrect_guesses):
    print("************")
    for line in hangman_art[incorrect_guesses]:
        print(line)

    print("************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    # select a random answer from the list
    answer = random.choice(answers).lower()

    # set the maximum number of incorrect guesses
    max_attempts = 6
    attempts_left = max_attempts

    hint = ["_"]*len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    print("Welcome to the hangman game")
    print(f"You have {max_attempts} incorrect guesses allowed")
    is_running = True

    while is_running and attempts_left > 0:
        display_hangman(wrong_guesses)
        display_hint(hint)
        print(f"Number of chances you have: {attempts_left}")
        guess = input("Enter a letter: ").lower()

        if (len(guess) != 1 or not guess.isalpha()):
            print("Invalid input, Please enter 1 character at a time")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed.")
            attempts_left -= 1
            wrong_guesses += 1
            os.system("clear")
            display_hangman(wrong_guesses)
            os.system("clear")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            attempts_left -= 1

        if "_" not in hint:
            os.system("clear")
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("You win")
            input()
            is_running = False
        elif attempts_left == 0:
            os.system("clear")
            display_hangman(wrong_guesses)
            print("You lose!")
            input()
            is_running = False
        os.system("clear")


if __name__ == "__main__":
    main()
