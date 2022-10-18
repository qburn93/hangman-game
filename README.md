

# Hangman game



## User stories
- User reports that program is running smooth.
- One user reported that they could not make out how many letters there is in the hidden word due to the lower cases __ being too close to each other, and now it is more visible after taking care of it.
## Program Features 

At the start, user is presented with input for their name.
When user has lost the game, the option to play again or end the program is featured.
Limit: It is the maximum guesses we provide to the user to guess a particular word.
Guess: Takes the input from the user for the guessed letter. Guess.strip() removes the letter from the given word.
If loop checks that if no input is given, or two letters are given at once, or a number is entered as an input, it tells the user about the invalid input and executes hangman again.

### Features Left to Implement
- Several difficulties, from hard to medium and easy.
- Saving high score.
- Add more visuals to intro/game immersion while playing.
- I would like to add some API features in the future, and maybe a google excel sheet of the high score or which words have the most lost games of the chosen words. This is nothing for the user though primarily a data-driven feature.

### Testing and fixed Bugs
- The program was tested manually with pep8:
 - Error messeges regarding character length of each code lines that I have had to shorten. 
 - Several indentation issues that made functions break while creating the program.
![Commentbugs](https://i.imgur.com/RcU8Aaj.png)


- 1. While trying to start a new game AFTER game is WON, the play again Y button just ends the game instead of restarting. But if game is lost, the restart of the game has no issues.
![newgamebug](https://i.imgur.com/nBZ7U90.png)
- 2. I tried changing to loop_game and play_game instead of calling for main function, but it still didn't fix the issue. 
- Update: I noticed when restarting the repository the play again feature works after game is won, and after a short while, it does not work again.
![y/newgame](https://i.imgur.com/gclN4UM.png)

- An error was caused by following line, where the word in play would not be displayed after game was lost. This was fixed by adding no blank space after the comma.
![wordwas](https://i.imgur.com/b3Z3MsT.png)

- 3. While trying to make clear space between _ _ to more easly see the ammount of letters, I ran into a bug that pushes the underscores + the letters that are guessed.I tried making a blank space on each side individualy and both to make spacing clear, but it didnt fix the issue.
![line](https://i.imgur.com/IhMrO7x.png)
- It caused this. Instead of replacing each underscore with the correct guessed letter.
![bug5](https://i.imgur.com/8sUGRmf.png)



### Validator Testing 
- Pep8 validator was added to the gitpod workspace since the website is not working 100%. Most errors were resolved, apart from variables names not conforming to UPPER_CASE naming style and some trailing white spaces and indentation errors that were taken care of.
Program was tested manually several times after each implementation of loop and validator functions.
- I tested the program for 2 hours to implement where and when to stop colorama—ie. changing color based on input or final game result.


### Unfixed Bugs

- I have a bug at an early stage where the get_valid_letter thinks every letter input is correct and it does not continue the game. It just congratulates for winning the game. Will update in future...
- UPDATE: There was a Blankspace indentation error on validate input function.
![validatorbug](https://i.imgur.com/7bYv6rq.png)

## Deployment

This game was deployed to github pages and Heroku.

# Heroku
- 1. Log into the [Heroku](https://dashboard.heroku.com/apps) website

  2. Click 'New' and choose 'Create new app'.

  3. Choose an app name (this does NOT have to be identical to GitHub) and a region.

  4. Click 'Create app'.
  ![createapp](https://i.imgur.com/rQkc1fe.png)
  5. You should be on the 'Deploy' tab (1).

  6. Choose connect to GitHub account (2).

  7. Search for the repository you want to deploy. The name needs to match exactly (3).

  8. Click 'Connect' (4).
  9. Select whether you want automatic deployment.
  10. Choose which branch you want to deploy.
  11. Click 'Deploy branch'
  12. When the deployment is complete, go to the 'Settings' page to configure vars and buildpacks.

  13. Click 'Reveal Config Vars'. For this project, we needed PORT 8000 (as a var) and the Node.js and Python buildpacks.

  14. Click 'Add' to fill out PORT and 8000 in he KEY / VALUE pair. This has been done.

  15. Click 'Add buildpack' and select Node.js from the options.

  16. Scroll back to the top where you will see 'Open app'. BEFORE opening, you will need to redeploy as the first deployment happened before Node.js was installed as a buildpack. If you open now, there will be an error.
<hr>

- Open the repository settings.
- Go to "pages" (found under "code and automation").
- Choose which branch to build from. You want to choose "main". Do not forget to save the settings.
- (If needed, choose a custom domain)
- Open the repository in github desktop (I used github desktop. You can do this in git too.)
- Choose to create a local clone (the first time you open your repository in github desktop, there should be a window asking if you want to create a clone)
- Copy the link to your deployed website (which can be found in the github pages settings, where you chose which branch to build from) and make sure it is operating as expected.
- The deployed website will now be updated when you push anything new to the repository.

The live link can be found here -  


## Credits 
- I want to credit CS students for inspiration and somewhat laying the mental ground image for me with my project.
[Video Link](https://www.youtube.com/watch?v=ynwB-QfOPRw&t=614s&ab_channel=CSStudents)
- Credit on how to implement time.sleep delay for increased immersion.
[Programiz](https://www.programiz.com/python-programming/time/sleep)


### Content 

__Programs Used__
  - Imported colorama for immersion while game is being played.
  - I tested the program for 2 hours to implement where and when to stop colorama. ie. changing color based on input or final game result.
  - Git was used for using the Gitpod terminal to commit to Git and push to Github.
  - Github - Github was used to store the project code and display the project in Github Pages. (https://github.com/)
 



#### Forking and cloning
- Forking is creating a new repository with the same content as the one you forked. 
    - This is done by going to the repository you want to clone and clicking the "fork" icon in the top right corner.
- Cloning is used for making local copies of your code.
    - Cloning a repository with github desktop is easily done by clicking the green "code" button and choosing the "open in github desktop" option. If you do not have a clone already, github desktop will ask if you want to create a local clone. Click yes.
    - If you do it with git you have to write "git clone" and then specify what you want to clone.

The live link can be found here - https://hangman-python-game.herokuapp.com/



 

