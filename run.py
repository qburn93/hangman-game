import random
import time
from words import words_to_guess
import colorama
from colorama import Fore, Back, Style
colorama.init()


# Starts steps to invite in the game


print(Fore.WHITE + Style.BRIGHT + "\nWelcome to\n")
time.sleep(0.5)
print("|----------------------|")
time.sleep(0.5)
print("|-----HANGMAN GAME-----|")
time.sleep(0.5)
print("|----------------------|")
time.sleep(1)
print(Fore.GREEN + "Game Rules are:\n")
print("1. You have 5 attempts to guess the correct word or else you lose.")
print('\033[39m')
name = input(Fore.CYAN + "Please Enter your name: ")
print('\033[39m')
print(Fore.MAGENTA + "Welcome " + name + "! Good luck!")
time.sleep(2)
print("Game is about to start!\n")
print('\033[39m')
time.sleep(3)

# Global variablies required to run game


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global lives

    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# Loop to re-execute the game when the first round ends


def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do you want to play again? y = yes, n = no \n")
    if play_game == "y":
        print(Fore.GREEN + "Let's go again!")
        print('\033[39m')
        main()
    elif play_game == "n":
        print(Fore.WHITE + Back.RED + Style.BRIGHT + "Thanks for playing!")
        print('\033[39m')
        exit()

# Declaring all variable required for the game


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Hangman word: " + display + " Enter your guess: ")
    guess = guess.strip()
    # Validate the input
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print(Fore.RED + "Invalid input, Try a letter\n")
        print('\033[39m')
        hangman()

    # If letter is guessed already
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    # If letter is incorrect
    elif guess in already_guessed:
        print("Already guessed that letter, try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(Fore.RED + "Wrong" + str(limit - count) + " guesses left\n")
            print('\033[39m')

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(Fore.RED + "Wrong" + str(limit - count) + " guesses left\n")
            print('\033[39m')

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(Fore.RED + "Wrong" + str(limit - count) + " guesses left\n")
            print('\033[39m')

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(Fore.RED + "Wrong" + str(limit - count) + " last guess\n")
            print('\033[39m')

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print(Fore.RED + "Wrong guess. You have lost!!\n")
            print('\033[39m')
            print("The word was:", already_guessed, word)
            print('\033[39m')
            play_loop()

    # If user has guessed all the letters
    if word == '_' * length:
        print(Back.CYAN + Style.BRIGHT + "Congrats! You have won the game")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()
