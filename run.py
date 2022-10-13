import random
import time
from hangman import draw_hangman

# Global Variable for correctly guessed letters(array)
correctly_guessed_letters = []

# Global Variable for incorrectly guessed letters(array)
incorrectly_guessed_letters = []

# Global Variable for randomly chosen word(string)
random_chosen_word = ""

# Global variable for lives left(integer)
lives_left = 6

# Global Variable for game over(boolian)
game_over = False


def random_word():
    """Returns a random selected word from our list of acceptable words"""
    global random_chosen_word
    
    words_list = [
        "Ambiguous",
        "Linear",
        "Extravagant",
        "Bali",
        "Singapore",
        "Institute",
        "University",
    ]
    # Generate random sequance of words from word list
    random.seed(time.time())
    random_chosen_word = random.choice(words_list)
    # Lower case to help do the comparison later on 
    random_chosen_word = random_chosen_word.lower()


def draw_word():
    """Dashed out letters that are not guessed yet"""
    global correctly_guessed_letters
    global random_chosen_word
    # Lopping through from 0 to the length of the random chosen word 
    for i in range(0, len(random_chosen_word)):
        letter = random_chosen_word[i]
        if letter in correctly_guessed_letters:
            print(letter, end=" ")
        # If word is not guessed yet it will be displayed with an underscore
        else:
            print("_", end=" ")
    




def get_valid_letter():
    """Makes sure the number of letters typed is different each time and is typed only once
        and is checking for validation"""
    is_leter_valid = False
    letter = ""
    while is_leter_valid is False:
        letter = input("Enter letter guess:\n")
        letter = letter.strip().lower()
        # Checks for error when inputs answers and validates that new letter
        if len(letter) <= 0 or len(letter) > 1:
            print("Letter must be of 1 length")
        elif letter.isalpha():
            if letter in correctly_guessed_letters or letter in incorrectly_guessed_letters:
                print("You have already guessed that letter" + letter + ", please try again")
            else:
                is_leter_valid = True
        else:
            print("letter must be (a-z)")
    
    return letter


def guess_letter():
    """Checks if the one letter guessed is correct or wrong, and updates global variables based on the result"""
    global correctly_guessed_letters
    global incorrectly_guessed_letters
    global lives_left

    letter = get_valid_letter()
    # Checks if guessed letter is in our random chosen word from list and appends it to either correct guess or wrong guess and subtracts by 1 life for wrong guess
    if letter in random_chosen_word:
        correctly_guessed_letters.append(letter)
    else:
        incorrectly_guessed_letters.append(letter)
        lives_left -= 1
 

def check_for_game_over():
    """Checks to see if player won or lost based on guesses left"""
    global lives_left
    global game_over
    global correctly_guessed_letters
    # Drawn the whole hangman picture if lives left equals to 0 else game is won and user is greeted with congratulations
    # Negative feed back loop checks this
    if lives_left <= 0:
        game_over = True
        draw_hangman()
        print("Game Over! The hidden word was" + random_chosen_word + ". Dont give up now! Try again")
    # Positive feedback loop assumes game is over because everything was correctly guessed
    # Iterates through every letter
    else:
        guessed_all_letters = True
        for letter in random_chosen_word:
            if letter not in correctly_guessed_letters:
                guessed_all_letters = False
                break
        if guessed_all_letters:
            game_over = True
            print("Winner! Congrats! You can play again if you like")

 
def main():
    """Entry point of application, calls all other methods in a loop"""
    global game_over
    
    
    print("-----------------")
    print("|The Hangman game|")
    print("-----------------")

    while game_over is False:
        draw_hangman()
        draw_word()

        if len(incorrectly_guessed_letters) > 0:
            print("Incorrect guesses: ")
            print(incorrectly_guessed_letters)

        guess_letter()
        check_for_game_over()


if __name__ == '__main__':
    """Will only be called when you run the pythron program from the terminal or an IDE like Pycharm"""

    main()
    
    