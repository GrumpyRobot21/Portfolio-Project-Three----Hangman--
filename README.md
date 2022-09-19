# **Hangman(with added sarcasm)**
Hangman(with added sarcasm) is written as a Python terminal game. This will run on the Code Institute terminal viewer on Heroku (until the Heroku free offering cconcludes in November 2022). A suitable alternative for hosting the live app following that date is currently being researched.

As per the standard Hangman rules, Users try to guess the word by inputting letters until they either guess the word or they lose all of their lives and forfeit the game. The target audience is anyone who likes to challenge themselves mentally with a guessing game. 

[Hangman(with added sarcasm)](https://hangman-pproj3.herokuapp.com/) - You can view the live site here. 

![Game-Page](images/home_page.jpg) 

## **Table of Contents**
 * [**How to Play**](#how-to-play)
 * [**Planning Stage**](#planning-stage)
 * [**Features**](#features)
 * [**Testing**](#testing)
 * [**Technologies Used**](#technologies-used)
 * [**Bugs**](#bugs)
 * [**Validators**](#validators)
 * [**Deployment**](#deployment)
 * [**Credits**](#credits)

## **How to Play**
Players play Hangman(with added sarcasm) by typing letters into the mock terminal. The purpose of the game is to guess the hidden word. The words are represented with empty dashes to show players how many letters they have to guess in order to win. when the player guesses a correct letter, the individual dashes are replaced with the correct letter. When a player buesses incorrectly, they will receive an error message and the playes lives will reduce by one. The player will then be invited to continue to input their guesses until thier total lives have run out or the word has been correctly guessed. 
The game is over either when the player has correctly guessed the word or they have run out of lives. 

## **Planning Stage**

### **User Goals**
To build a terminal based game of Hangman for user to mentally challenge themselves in a fun gaming environment.
 * The game rules and environment should be easily interpreted and accessible for a user.
 * The game should definitely be lots of fun to play.
 * It should be suitably challenging and encourage users to replay many times.

 ### **Using FlowCharts**
 During the planning process in order to assist with the development progress and to figure out the linear process of the game I created the following flowchart.
  * Where were inputs from the user needed?
  * How would I deal with invalid inputs or incorrect tries?
  * Were there any logic errors that could perceivably break the game?

![Design FlowChart](images/hangman_flow.jpg) 

 ## **Features**

 ### **Existing Features**
* Home/Start page
  * Explains Game play to user
  * Explains how to continue

  ![Home page](docs/read-me/main-menu.png)

* Choose challenge difficulty
  * 'Lemon Squeezy' = 10 lives
  * 'King of the Swingers!' = 5 lives

![Choose difficulty](docs/read-me/difficulty.png)

* View Game Rules

![View game rules](docs/read-me/rules.png)

 * Random word generations
   * A function randomly generates a word from a list of 500 words.
   * The player can not see what the word is but can see how many letters are in the word denoted by _ _ _ _ _ 

![Game play](docs/read-me/amount-of-letters.png) 

 * Lives with graphical representation
   * Depending on difficilty level chosen, the user has a limited amount of lives before game ends.
   * Graphically represented while playing the game.
  
![Ammount of Lives](docs/read-me/hangman-graphic.png) 

* Game Over Screens.
 * A custom screen for winning the game and for game over. 
 * Users can choose whether to restart the game or go back to the main menu.

![You Win!](docs/read-me/you-win.png) 

![You lose!](docs/read-me/game-over.png) 

* Checks for invalid inputs.
  * For all user inputs, checks are run to ensure there are no invalid inputs submitted.
  * For any invalid submissions, a tailored error message is displayed and the user is prompted to input their selection again.

