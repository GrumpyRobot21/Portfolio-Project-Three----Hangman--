import random  # random choice method
from gamewords import words  # custom gameword list
import keyboard  # hotkey support for user interaction
import string  # ascii alphabet function
import time  # time sleep function
import pyfiglet  # big letter graphics module


class Colortext:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    YELLOW = '\033[1;33m'
    BOLD = '\033[1m'


def start_intro():
    """
    Generates game options for player: intro to the game, difficulty, rules.
    """
    print(Colortext.BOLD + Colortext.YELLOW + """
        _____________________________________________
       |_____________________________________________|
         ||                              \ \     |  |
         ||                               \ \    |  |
        /==\                               \ \   |  |
       |____|                               \ \  |  |
       |____|                                \ \ |  |
       |____|                                 \ \|  |
       //  \\\                                  \ |  |
      //    \\\                                  \|  |
     //      \\\                                  |  |
    ||        ||
    ||        ||
    ||        ||
     \\\      // 
      \\\    //
       \\\__// 
    """)
    print(Colortext.BLUE + Colortext.BOLD + "Welcome to ye olde game of HANGMAN!!!!\n\nYou the player must carefully select letters in the vain hope of avoiding the gallows \nby guessing the word before it's too late!\n\nCan you cheat the hangmans noose in time?  Find out....if you dare!\n")

    print(Colortext.BLUE + Colortext.BOLD + "Enter " +Colortext.GREEN + Colortext.BOLD + "'p' "+ Colortext.BLUE + Colortext.BOLD +  "to continue: ")

    run = input('\n')
    if run != ('p'):
        print(Colortext.GREEN + Colortext.BOLD +"\n\nWRONG KEY!!! (I would go for the easy setting if I were you...). \n\nPress 'p' to continue: ")
        time.sleep(3)
        print('\033c', end='')  # clears the console - \033 is the ASCII escape character.
        start_intro()
    else:
        print(Colortext.YELLOW + Colortext.BOLD + '\n\nGOOD LUCK!')
        time.sleep(2)
        print('\033c', end='')  # clears the console - \033 is the ASCII escape character.
        game_rules()


def game_rules():
    """
    Rules for gameplay and player difficulty selection
    """
    print(Colortext.GREEN + Colortext.BOLD + player_lives(10))
    print(Colortext.RED + Colortext.BOLD + "Select your difficulty level from the choices below and the challenge will \nbegin. See you at the end .......of the rope! \n\nEnter" + Colortext.BLUE + Colortext.BOLD +" '1' " + Colortext.RED + Colortext.BOLD + "for difficulty level - " + Colortext.YELLOW + "'Lemon Squeezy' " + Colortext.RED + Colortext.BOLD + "\nalso known as:" + Colortext.YELLOW + "\n'I can see the pub from up here!' \n\n" + Colortext.RED + Colortext.BOLD + "Enter" + Colortext.BLUE + Colortext.BOLD + " '2' " + Colortext.RED + Colortext.BOLD + "for difficulty level - " + Colortext.YELLOW + "'King of the Swingers!' " + Colortext.RED + Colortext.BOLD + "\nalso known as:" + Colortext.YELLOW + "\n'That's a smidge on the tight side, cough cough!'")

    choose = input('\n')

    if choose == '1':  # Player selects easiest challenge setting.
        lives = 10
        print(Colortext.GREEN + Colortext.BOLD + "\n\nPlaying it safe eh? or maybe prolonging the agony.....They do say that waiting is the worst!! \n\nAll that nervous anticipation.....! ")
        time.sleep(5)  # 5 second delay
        print('\033c', end='')  # clears the console - \033 is the ASCII escape character.
        play_game(hang_word, lives)
    elif choose == '2':  # Player selects difficult challenge setting.
        lives = 5
        print(Colortext.GREEN + Colortext.BOLD + "\n\nOoh, you're feeling brave aren't you!\n\nThis won't take long! ")
        time.sleep(5)  # 5 second delay
        print('\033c', end='')  # clears the console - \033 is the ASCII escape character.
        play_game(hang_word, lives)
    else:  # Error message for incorrect choice.
        print(Colortext.GREEN + Colortext.BOLD + "\n\nNot getting the 'hang' of this are you? (you see what I did there?).\n\nLet's try this again...  \n\nChoose either 1 or 2 to get this show on the road!")
        time.sleep(5)  # 5 second delay
        print('\033c', end='')  # clears the console - \033 s the ASCII escape character.
        game_rules()

def choose_word():
    """
    Random word selector for the game
    """
    word = random.choice(words)
    return word.upper()  # returns the random game word in upper case 


hang_word = choose_word()  # defining a variable for the game function               