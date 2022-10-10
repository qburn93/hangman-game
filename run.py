# Global Variable for correctly guessed letters(array)
correctly_guessed_letters = []

# Global Variable for incorrectly guessed letters(array)
incorrectly_guessed_letters = []

# Global Variable for randomly chosen word(string)
random_chosen_word = ""

# Global variable for lives left(integer)
lives_left = 7

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
    # Generate random sequance of words from list
    random.seed(time.time())
    random_chosen_word = random.choice(words_list)
    random_chosen_word = random_chosen_word.lower()

def draw_word():
    """Dashed out letters that are not guessed yet"""
    pass


def draw_hangman():
    """Hangman printed based on number of guesses left"""
    pass


def get_valid_letter():
    """Makes sure the number of letters typed is different each time and is typed only once"""
    pass


def guess_letter():
    """Checks if the one letter guessed is correct or wrong, and updates global variables based on the result"""
    pass
 

 def check_for_game_over():
    """Checks to see if player won or lost based on guesses left"""
    pass

 
 def main():
    """Entry point of application, calls all other methods in a loop"""
    pass