# Global Variable for correctly guessed letters(array)
correctly_guessed_letters = []

# Global Variable for incorrectly guessed letters(array)
incorrectly_guessed_letters = []

# Global Variable for randomly chosen word(string)
random_chosen_word = ""

# Global variable for lives left(integer)
lives_left = 6

# global Variable for game over(boolian)
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
    # Lower case to help do the comparison later on to make sure we're not comparing an uppercase letter to a lowercase 
    random_chosen_word = random_chosen_word.lower()

def draw_word():
    """Dashed out letters that are not guessed yet"""
    global correctly_guessed_letters
    global random_chosen_word
    # Lopping through from 0 to the length of the random chosen word and if that letter is guessed it will be displayed with a space at the end
    for i in range(0, len(random_chosen_word)):
        letter = random_chosen_word[i]
        if letter in correctly_guessed_letters:
            print(letter, end=" ")
        #If word is not guessed yet it will be displayed with an underscore bar
        else:
            print("_", end=" ")
    


def draw_hangman():
    """Hangman printed based on number of guesses left"""
    global lives_left

    if lives_left == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           /")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")


def get_valid_letter():
    """Makes sure the number of letters typed is different each time and is typed only once
        and is checking for validation"""
    is_leter_valid = False
    letter = ""
    while is_leter_valid is False:
        letter = input("Enter letter guess: ")
        letter = letter.strip().lower()


def guess_letter():
    """Checks if the one letter guessed is correct or wrong, and updates global variables based on the result"""
    pass
 

 def check_for_game_over():
    """Checks to see if player won or lost based on guesses left"""
    pass

 
 def main():
    """Entry point of application, calls all other methods in a loop"""
    pass