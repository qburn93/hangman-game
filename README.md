

# Hangman game



## User stories

## Program Features 

At the start user is presented with input for their name.
When user has lost the game, the option to play again or end the program is featured.
Limit: It is the maximum guesses we provide to the user to guess a particular word.
Guess: Takes the input from the user for the guessed letter. Guess.strip() removes the letter from the given word.
If loop checks that if no input is given, or two letters are given at once, or a number is entered as an input, it tells the user about the invalid input and executes hangman again.

### Features Left to Implement


### Testing and fixed Bugs
- The program was tested manually with pep8:
 
![Commentbugs](https://i.imgur.com/QJzs45l.png)
![indentbug](https://i.imgur.com/72uHhKL.png)
- While trying to start a new game AFTER game is WON, the play again Y button just ends the game instead of restarting. But if game is lost the restart of the game has no issues.
![newgamebug](https://i.imgur.com/MZGQAcP.png)
- An error was caused by following line, where the word in play would not be displayed after game was lost, this was fixed by adding no blank space after the comma.
![wordwas](https://i.imgur.com/b3Z3MsT.png)




### Validator Testing 



### Unfixed Bugs

- I have a bug at an early stage where the get_valid_letter thinks every letter input is correct and it does not continue the game it just congratulates for winning the game. Will update in future...
![validatorbug](https://i.imgur.com/7bYv6rq.png)

## Deployment

This game was deployed to github pages.

- Open the repository settings.
- Go to "pages" (found under "code and automation").
- Choose which branch to build from. You want to choose "main". Do not forget to save the settings.
- (If needed, choose a custom domain)
- Open the repository in github desktop (I used github desktop. You can do this in git too.)
- Choose to create a local clone (the first time you open your repository in github desktop, there should be a window asking if you want to create a clone)
- Copy the link to your deployed website (which can be found in the github pages settings, where you chose which branch to build from) and make sure it is operating as expected.
- The deployed website will now be updated when you push anything new to the repository.

The live link can be found here - https://bogdan933.github.io/Quiz-App---Project-2/ 


## Credits 



### Content 

__Programs Used__
  - Git was used for using the Gitpod terminal to commit to Git and push to Github.
  - Github - Github was used to store the project code and display the project in Github Pages. (https://github.com/)
 



#### Forking and cloning
- Forking is creating a new repository with the same content as the one you forked. 
    - This is done by going to the repository you want to clone, and clicking the "fork" icon in the top right corner.
- Cloning is used for making local copies of your code.
    - Cloning a repository with github desktop is easily done by clicking the green "code" button and choosing the "open in github desktop" option. If you do not have a clone already, github desktop will ask if you want to create a local clone. Click yes.
    - If you do it with git you have to write "git clone" and then specify what you want to clone.

The live link can be found here - 



 

